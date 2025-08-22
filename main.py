from flask import Flask, request, jsonify
import pywhatkit as kit
import datetime

app = Flask(__name__)


@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()

    try:
        phone = data['phone']
        message = data['message']

        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1  # precisa agendar no futuro

        kit.sendwhatmsg(phone, message, hour, minute, wait_time=10, tab_close=True)

        return jsonify({"status": "success", "message": "Mensagem agendada com sucesso!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

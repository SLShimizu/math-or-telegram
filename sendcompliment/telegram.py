
# importing all required libraries
import requests

def sendstuff():
    requests.get("https://api.telegram.org/bot5328440553:AAGzWoIgUB0KBjtlJG-063KTdx7PhMsH-L0/sendMessage?chat_id=-769391165&text=Have a wonderful day, you are awesome")


if __name__ == "__main__":
    # Le Wagon location
    sendstuff()
    print('check your message')

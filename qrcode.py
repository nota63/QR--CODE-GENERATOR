# PROJECT QR CODE GENERATOR
import qrcode as qr
from plyer import notification
import datetime
import time


class QR:
    def __init__(self):
        self.codes = []

    #      FUNCTION TO GENERATE QR CODE

    def generate_qr(self):
        image = qr.make(input('Enter link, media, directory, or any other to generate qr:'))
        input('Press Enter to generate QR!')
        image.save('generated_qr_b_python.png')
        self.codes.append(image)
        notification.notify(
            title='QR-CODE-GENERATOR-{}'.format(datetime.date.today()),
            message=f" QR Code Generated Successfully For -- {image}\n You can view it in your project directory!",
            timeout=7
        )
        print('Done')

    def view_codes(self):
        input('press enter to view qr-codes generated till now')
        for code in self.codes:
            print(f'code: {code}')


def main():
    code = QR()
    while True:
        try:
            menu = 'press [1] for generate qr\n press [2] for view_generated codes'
            print(menu.upper())

            user1 = int(input('enter index to start:'))
            if user1 == 1:
                code.generate_qr()

            elif user1 == 2:
                code.view_codes()

        except ValueError:
            print('value error!')
        except IndexError:
            print('indexError!')


if __name__ == "__main__":
    main()

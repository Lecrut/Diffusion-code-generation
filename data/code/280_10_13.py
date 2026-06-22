class Repeater:
    COUNT = 5

    @staticmethod
    def repeat_action():
        message = "Repeat an action five times now"
        for _ in range(Repeater.COUNT):
            print(message)

if __name__ == '__main__':
    Repeater.repeat_action()
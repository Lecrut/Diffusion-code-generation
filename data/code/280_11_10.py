class Repeater:
    REPEAT_COUNT = 3

    @staticmethod
    def perform_repeating_action():
        action = "Action"
        print(f"Performing '{action}' {Repeater.REPEAT_COUNT} times:")
        for _ in range(Repeater.REPEAT_COUNT):
            print(action)

if __name__ == '__main__':
    Repeater.perform_repeating_action()
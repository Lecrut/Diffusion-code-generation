import time

class Repeater:
    DELAY_SECONDS = 1

    @staticmethod
    def repeat_action(action_string: str, num_times: int) -> None:
        for _ in range(num_times):
            print(action_string)
            time.sleep(Repeater.DELAY_SECONDS)

if __name__ == '__main__':
    repeater = Repeater()
    action = "Hello World"
    count = 5
    repeater.repeat_action(action, count)
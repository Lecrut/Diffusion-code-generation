import time

class Repeater:
    DELAY_SECONDS = 1

    @staticmethod
    def delay():
        time.sleep(Repeater.DELAY_SECONDS)

    def repeat_action(self, action_string: str, num_times: int):
        result = ""
        for _ in range(num_times):
            result += action_string + "\n"
            self.delay()
        return result.strip()

if __name__ == '__main__':
    repeater = Repeater()
    action = "Hello World"
    count = 5
    output = repeater.repeat_action(action, count)
    print(output)
import time

class ActionRepeater:
    DELAY_SECONDS = 1
    
    @staticmethod
    def repeat_action(action_string, num_times):
        result = ""
        for _ in range(num_times):
            result += action_string + "\n"
            time.sleep(ActionRepeater.DELAY_SECONDS)
        return result.strip()

if __name__ == '__main__':
    repeater = ActionRepeater()
    action = "Hello World"
    count = 5
    output = repeater.repeat_action(action, count)
    print(output)
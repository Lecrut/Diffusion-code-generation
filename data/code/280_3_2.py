class Repeater:
    def repeat_action(self, action_string: str, times: int) -> str:
        result = ""
        for _ in range(times):
            result += action_string + "\n"
        return result.strip()
if __name__ == '__main__':
    repeater = Repeater()
    action = "Hello World"
    count = 3
    output = repeater.repeat_action(action, count)
    print(output)
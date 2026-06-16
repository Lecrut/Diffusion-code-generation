class Repeater:
    def repeat(self, action_string: str, num_times: int) -> str:
        result = ""
        for _ in range(num_times):
            result += action_string + "\n"
        return result.strip()
if __name__ == '__main__':
    repeater = Repeater()
    action = "Hello World"
    count = 3
    output = repeater.repeat(action, count)
    print(output)
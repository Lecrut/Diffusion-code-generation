class Repeater:
    def repeat_action(self, action_string, num_times):
        result = ""
        for _ in range(num_times):
            result += action_string + "\n"
        return result
if __name__ == '__main__':
    repeater = Repeater()
    action = "Hello World"
    count = 3
    output = repeater.repeat_action(action, count)
    print(output)
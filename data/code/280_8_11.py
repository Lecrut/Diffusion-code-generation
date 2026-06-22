class ActionRepeater:
    def __init__(self):
        self.result_list = []

    def repeat_action(self, times):
        if times == 0:
            return
        action_result = f"Action {times}"
        self.result_list.append(action_result)
        self.repeat_action(times - 1)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeater.repeat_action(10)
    print(repeater.result_list)
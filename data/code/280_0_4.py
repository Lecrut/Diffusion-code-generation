class ActionRepeater:
    def repeat_action(self, times):
        for i in range(times):
            print(f"Iteration {i + 1}")

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeater.repeat_action(10)
class ActionRepeater:
    def __init__(self, max_repeats):
        self.max_repeats = max_repeats

    def repeat_action(self):
        for _ in range(self.max_repeats):
            print("Action repeated")
            if _ == 2:
                break

if __name__ == '__main__':
    repeater = ActionRepeater(3)
    repeater.repeat_action()
class ActionRepeater:
    def __init__(self):
        self.message = "Repeat an action five times now"

    def repeat_action(self, count):
        for _ in range(count):
            print(self.message)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeater.repeat_action(5)
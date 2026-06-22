class ActionRepeater:
    def __init__(self, message):
        self.message = message

    def repeat(self, times):
        for _ in range(times):
            print(self.message)

if __name__ == '__main__':
    repeater = ActionRepeater('Repeat an action five times now')
    repeater.repeat(5)
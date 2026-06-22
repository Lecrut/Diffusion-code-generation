class SequenceRepeater:
    def __init__(self):
        self.actions = ["Action One", "Action Two", "Action Three", "Action Four", "Action Five"]

    def repeat(self):
        for action in self.actions:
            print(action)

if __name__ == '__main__':
    repeater = SequenceRepeater()
    repeater.repeat()
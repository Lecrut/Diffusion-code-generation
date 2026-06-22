class SequenceRepeater:
    def __init__(self, action):
        self.action = action

    def repeat(self):
        for _ in range(5):
            self.action()

def sample_action():
    print("Action repeated")

if __name__ == '__main__':
    repeater = SequenceRepeater(sample_action)
    repeater.repeat()
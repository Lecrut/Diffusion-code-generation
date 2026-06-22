class SequenceRepeater:
    DEFAULT_ACTION = "Action repeated"
    
    @staticmethod
    def repeat(action=DEFAULT_ACTION):
        for _ in range(5):
            print(action)

if __name__ == '__main__':
    repeater = SequenceRepeater()
    repeater.repeat()
class SequenceRepeater:
    MAX_REPETITIONS = 5

    @staticmethod
    def repeat_action(action):
        for _ in range(SequenceRepeater.MAX_REPETITIONS):
            action()

if __name__ == '__main__':
    def sample_action():
        print("Action repeated")

    SequenceRepeater.repeat_action(sample_action)
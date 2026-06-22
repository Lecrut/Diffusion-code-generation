class Repeater:
    MAX_REPETITIONS = 10

    @staticmethod
    def repeat_action(action):
        count = 0
        while count < Repeater.MAX_REPETITIONS:
            action()
            count += 1

def sample_action():
    print("Action repeated")

if __name__ == '__main__':
    Repeater.repeat_action(sample_action)
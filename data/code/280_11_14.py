class Repeater:
    MAX_REPETITIONS = 3

    @staticmethod
    def repeat_operation():
        print("Operation repeated")

if __name__ == '__main__':
    for _ in range(Repeater.MAX_REPETITIONS):
        Repeater.repeat_operation()
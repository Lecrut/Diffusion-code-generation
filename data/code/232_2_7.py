import itertools

class NumberSequence:
    def __init__(self, start=1):
        self.count = itertools.count(start)

    def get_next_number(self):
        return next(self.count)

if __name__ == '__main__':
    sequence = NumberSequence()
    for _ in range(20):
        print(sequence.get_next_number())
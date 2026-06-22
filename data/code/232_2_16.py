import itertools

class NumberSequence:
    def __init__(self):
        self.sequence = list(itertools.count(1))

    def print_sequence(self, count=20):
        for number in self.sequence[:count]:
            print(number)

if __name__ == '__main__':
    sequence_instance = NumberSequence()
    sequence_instance.print_sequence()
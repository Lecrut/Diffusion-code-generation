from operator import add

class SequenceRepeater:
    def __init__(self, start):
        self.sequence = [start]

    def extend_sequence(self, factor):
        for _ in range(factor):
            self.sequence.extend([self.sequence[0]] * factor)

if __name__ == '__main__':
    repeater = SequenceRepeater('a')
    repeater.extend_sequence(3)
    print(''.join(repeater.sequence))

    repeater = SequenceRepeater('123')
    repeater.extend_sequence(2)
    print(''.join(repeater.sequence))
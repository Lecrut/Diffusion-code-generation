import operator

class SequenceRepeater:
    def __init__(self, sequence):
        self.sequence = sequence

    def repeat(self, factor):
        extended_sequence = operator.mul(self.sequence, factor)
        self.sequence.extend(extended_sequence)

if __name__ == '__main__':
    repeater = SequenceRepeater(['a', 'b', 'c'])
    repeater.repeat(3)
    print(repeater.sequence)
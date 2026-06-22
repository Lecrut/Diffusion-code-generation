def repeat_sequence(sequence, count):
    return sequence * count

class SequenceRepeater:
    def __init__(self, initial_sequence):
        self.sequence = initial_sequence
    
    def repeat(self, count):
        return self.sequence * count

if __name__ == '__main__':
    repeater = SequenceRepeater([1, 2, 3])
    print(repeater.repeat(3))
    print(repeater.repeat(5))
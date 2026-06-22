import numpy as np

class NumberSequence:
    def generate_sequence(self, start=1, end=25):
        return np.arange(start, end + 1)

if __name__ == '__main__':
    generator = NumberSequence()
    sequence = generator.generate_sequence()
    print(sequence)
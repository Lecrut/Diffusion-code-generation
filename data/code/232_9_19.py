import numpy as np

class NumberSequenceGenerator:
    def generate_sequence(self, start=1, end=25):
        return np.arange(start, end + 1)

if __name__ == '__main__':
    generator = NumberSequenceGenerator()
    sequence = generator.generate_sequence()
    print(sequence)
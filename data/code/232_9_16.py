import numpy as np

class NumberSequenceGenerator:
    START = 1
    END = 25
    
    @staticmethod
    def generate_sequence():
        return np.arange(NumberSequenceGenerator.START, NumberSequenceGenerator.END + 1)

if __name__ == '__main__':
    sequence = NumberSequenceGenerator.generate_sequence()
    print(sequence)
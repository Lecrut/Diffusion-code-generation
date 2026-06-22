import numpy as np

class NumberSequenceGenerator:
    def __init__(self, start=1, end=25):
        self.start = start
        self.end = end
    
    def generate_sequence(self):
        return np.arange(self.start, self.end + 1)
    
    def print_sequence(self):
        sequence = self.generate_sequence()
        for num in sequence:
            print(num)

if __name__ == '__main__':
    generator = NumberSequenceGenerator()
    generator.print_sequence()
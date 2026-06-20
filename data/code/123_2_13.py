import math

class FloatingPointSum:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_sum(self):
        return math.fsum(self.numbers)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    calculator = FloatingPointSum(sample_values)
    total = calculator.calculate_sum()
    print(total)
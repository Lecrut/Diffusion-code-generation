import math

class FloatingPointSum:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def sum_floating_points(self):
        return math.fsum(self.numbers)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3]
    calculator = FloatingPointSum(sample_values)
    total = calculator.sum_floating_points()
    print(total)
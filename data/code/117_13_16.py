import numpy as np

class ArrayDifferenceCalculator:
    def __init__(self):
        self.array1 = np.array([i for i in range(10000)])
        self.array2 = np.array([i * 2 for i in range(10000)])

    def calculate_difference(self):
        return self.array2 - self.array1

if __name__ == '__main__':
    calculator = ArrayDifferenceCalculator()
    difference_array = calculator.calculate_difference()
    print(difference_array)
import numpy as np

class NumberSumCalculator:
    def __init__(self):
        self.nums = None

    def set_numbers(self, numbers):
        if all(isinstance(num, (int, float)) for num in numbers):
            self.nums = np.array(numbers)
        else:
            raise ValueError("All elements must be numbers.")

    def sum_numbers(self):
        if self.nums is not None:
            return np.sum(self.nums)
        else:
            raise ValueError("Numbers have not been set yet.")

if __name__ == '__main__':
    calculator = NumberSumCalculator()
    sample_numbers = [10, 25, 3.5, 42]
    try:
        calculator.set_numbers(sample_numbers)
        result = calculator.sum_numbers()
        print("Total sum:", result)
    except ValueError as e:
        print(e)
from functools import reduce

class SumCalculator:
    def __init__(self):
        self.total = 0

    def add_to_total(self, number):
        self.total += number

    def get_total(self):
        return self.total

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_numbers = [1, 2, 3, 4, 5]
    for number in sample_numbers:
        calculator.add_to_total(number)
    print(f"Total of {sample_numbers}: {calculator.get_total()}")
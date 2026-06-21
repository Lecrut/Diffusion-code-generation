class LengthCalculator:

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def calculate_ratio(self):
        if self.length2 == 0:
            raise ValueError('The second length cannot be zero.')
        return self.length1 / self.length2
if __name__ == '__main__':
    calculator = LengthCalculator(15.6789, 3.4567)
    try:
        ratio = calculator.calculate_ratio()
        print(f'The ratio of {calculator.length1} to {calculator.length2} is: {ratio:.10f}')
    except ValueError as e:
        print(e)
    calculator.length1 = 22.3456
    calculator.length2 = 7.8901
    try:
        ratio = calculator.calculate_ratio()
        print(f'The ratio of {calculator.length1} to {calculator.length2} is: {ratio:.10f}')
    except ValueError as e:
        print(e)
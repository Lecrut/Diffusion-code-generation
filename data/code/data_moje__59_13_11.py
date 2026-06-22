class DigitSumCalculator:
    def __init__(self, number):
        self.number = number
        self.digits = [int(d) for d in str(number)]

    def calculate_sum(self):
        return sum(self.digits)

    def get_digits(self):
        return self.digits

if __name__ == '__main__':
    calculator_one = DigitSumCalculator(123)
    print(calculator_one.calculate_sum())
    print(calculator_one.get_digits())

    calculator_two = DigitSumCalculator(456)
    print(calculator_two.calculate_sum())
    print(calculator_two.get_digits())

    calculator_three = DigitSumCalculator(7890)
    print(calculator_three.calculate_sum())
    print(calculator_three.get_digits())
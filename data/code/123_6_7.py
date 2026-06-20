class DigitSumCalculator:
    def __init__(self, number):
        self.number = abs(number)

    def sum_of_digits(self):
        return sum(int(digit) for digit in str(self.number))

if __name__ == '__main__':
    calculator = DigitSumCalculator(12345)
    print(calculator.sum_of_digits())
    calculator.number = -9876
    print(calculator.sum_of_digits())
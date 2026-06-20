class DigitSumCalculator:
    def __init__(self):
        self.digit_map = {str(i): i for i in range(10)}

    def sum_of_digits(self, n):
        return sum(self.digit_map[digit] for digit in str(abs(n)))

if __name__ == '__main__':
    calculator = DigitSumCalculator()
    print(calculator.sum_of_digits(12345))
    print(calculator.sum_of_digits(-9876))
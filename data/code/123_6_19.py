class DigitSumCalculator:
    DIGIT_MAP = {str(i): i for i in range(10)}

    @staticmethod
    def sum_of_digits(n):
        return sum(DigitSumCalculator.DIGIT_MAP[digit] for digit in str(abs(n)))

if __name__ == '__main__':
    calculator = DigitSumCalculator()
    print(calculator.sum_of_digits(12345))
    print(calculator.sum_of_digits(-9876))
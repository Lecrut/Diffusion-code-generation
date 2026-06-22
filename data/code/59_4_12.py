class DigitSumCalculator:
    def __init__(self, number: int):
        self.number = number

    def calculate(self) -> int:
        if self.number == 0:
            return 0
        n = abs(self.number)
        total = 0
        digits_str = str(n)
        for char in digits_str:
            digit_val = ord(char) - 48
            total += digit_val
        return total

if __name__ == '__main__':
    samples = [54321, -998877, 0, 1000000000000000000]
    for val in samples:
        calc = DigitSumCalculator(val)
        print(calc.calculate())
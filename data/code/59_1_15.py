class DigitSum:
    def __init__(self, n):
        self.n = n

    def get_sum(self):
        return sum(int(digit) for digit in str(abs(self.n)))

    def get_digits(self):
        return [int(digit) for digit in str(abs(self.n))]

if __name__ == '__main__':
    sample_val = 4567
    d = DigitSum(sample_val)
    print(d.get_sum())
    print(d.get_digits())
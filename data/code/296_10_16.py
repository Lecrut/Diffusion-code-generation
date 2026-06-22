class Ratio:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def to_string(self):
        return f"{self.numerator}:{self.denominator}"

    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

def calculate_ratio(ratio_a, ratio_b):
    numerator_a, denominator_a = ratio_a.numerator, ratio_a.denominator
    numerator_b, denominator_b = ratio_b.numerator, ratio_b.denominator
    new_numerator = numerator_a * denominator_b + numerator_b * denominator_a
    new_denominator = denominator_a * denominator_b
    return Ratio(new_numerator, new_denominator)

if __name__ == '__main__':
    r1 = Ratio(2, 3)
    r2 = Ratio(4, 5)
    result_ratio = calculate_ratio(r1, r2)
    result_ratio.simplify()
    print(f"Resulting Ratio: {result_ratio.to_string()}")
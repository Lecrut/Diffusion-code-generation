class FractionSimplifier:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = num
        self.den = den
    
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def simplify(self):
        divisor = FractionSimplifier.gcd(self.num, self.den)
        return (self.num // divisor, self.den // divisor)

if __name__ == '__main__':
    initial_num = 10
    initial_den = 5
    simplifier = FractionSimplifier(initial_num, initial_den)
    simplified_ratio = simplifier.simplify()
    print(f"Simplified ratio: {simplified_ratio[0]}/{simplified_ratio[1]}")
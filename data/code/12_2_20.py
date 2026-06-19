class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        gcd = self.gcd(ratio_a, ratio_b)
        return ratio_a // gcd, ratio_b // gcd

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    converter = RatioConverter()
    simplified_ratio = converter.simplify(48, 18)
    print(simplified_ratio)
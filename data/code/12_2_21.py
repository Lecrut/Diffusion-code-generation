class RatioConverter:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self, ratio_a, ratio_b):
        divisor = self.gcd(ratio_a, ratio_b)
        return ratio_a // divisor, ratio_b // divisor

if __name__ == '__main__':
    converter = RatioConverter()
    simplified_ratio = converter.simplify(1024, 512)
    print(simplified_ratio)
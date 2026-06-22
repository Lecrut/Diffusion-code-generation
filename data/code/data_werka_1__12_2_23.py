class RatioConverter:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self, ratio_a, ratio_b):
        common_divisor = self.gcd(ratio_a, ratio_b)
        simplified_a = ratio_a // common_divisor
        simplified_b = ratio_b // common_divisor
        return simplified_a, simplified_b

if __name__ == '__main__':
    converter = RatioConverter()
    result = converter.simplify(48, 180)
    print(result)
class RatioConverter:

    def simplify(self, ratio_a, ratio_b):

        def gcd(a, b):
            while b != 0:
                a, b = (b, a % b)
            return a
        common_divisor = gcd(ratio_a, ratio_b)
        simplified_a = ratio_a // common_divisor
        simplified_b = ratio_b // common_divisor
        return (simplified_a, simplified_b)
if __name__ == '__main__':
    converter = RatioConverter()
    result = converter.simplify(48, 180)
    print(result)
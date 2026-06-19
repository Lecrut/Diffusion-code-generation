class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        gcd = self.euclidean_algorithm(ratio_a, ratio_b)
        return ratio_a // gcd, ratio_b // gcd

    def euclidean_algorithm(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    converter = RatioConverter()
    simplified_ratio = converter.simplify(24, 36)
    print(simplified_ratio)
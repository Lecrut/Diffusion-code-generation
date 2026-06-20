class Multiplier:
    def __init__(self, factor_a, factor_b):
        self.factor_a = factor_a
        self.factor_b = factor_b

    def calculate_product(self):
        return self.factor_a * self.factor_b

if __name__ == '__main__':
    multiplier = Multiplier(42, 7)
    print(multiplier.calculate_product())
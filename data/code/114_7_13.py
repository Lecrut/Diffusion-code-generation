class Multiplier:
    def __init__(self, constant):
        self.constant = constant

    def multiply(self, value):
        return value * self.constant

if __name__ == '__main__':
    multiplier_double = Multiplier(2)
    result_double = multiplier_double.multiply(3)
    print(f"multiply(3, 2): {result_double}")

    multiplier_triple = Multiplier(3)
    result_triple = multiplier_triple.multiply(4)
    print(f"multiply(4, 3): {result_triple}")
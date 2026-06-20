class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def multiply(self, value):
        return value * self.factor

if __name__ == '__main__':
    multiplier_double = Multiplier(2)
    multiplier_triple = Multiplier(3)
    print(f"multiplier_double.multiply(5): {multiplier_double.multiply(5)}")
    print(f"multiplier_triple.multiply(6): {multiplier_triple.multiply(6)}")
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, value):
        return value * self.factor

if __name__ == '__main__':
    multiplier5 = Multiplier(5)
    multiplier10 = Multiplier(10)
    result_double = multiplier5.multiply(4)
    result_triple = multiplier10.multiply(3)
    print(f"double(4): {result_double}")
    print(f"triple(3): {result_triple}")
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, value):
        return value * self.factor

if __name__ == '__main__':
    double_instance = Multiplier(2)
    triple_instance = Multiplier(3)
    print(f"double(4): {double_instance.multiply(4)}")
    print(f"triple(5): {triple_instance.multiply(5)}")
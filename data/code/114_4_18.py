class Multiplier:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_product(self):
        return self.a * self.b

if __name__ == '__main__':
    multiplier_instance = Multiplier(42, 7)
    product = multiplier_instance.calculate_product()
    print(product)
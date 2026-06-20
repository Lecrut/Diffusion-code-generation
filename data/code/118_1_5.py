class FigureProduct:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b

if __name__ == '__main__':
    product_instance = FigureProduct(4, 5)
    print(product_instance.calculate())
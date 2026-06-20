class FigureProduct:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 * self.num2

if __name__ == '__main__':
    product_instance = FigureProduct(5, 3)
    print(product_instance.calculate())
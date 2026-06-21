class ProductCalculator:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_product(self):
        total_product = 1
        for product in self.products:
            total_product *= product[0]
        return total_product

if __name__ == '__main__':
    calculator = ProductCalculator()
    calculator.add_product((2,))
    calculator.add_product((3,))
    calculator.add_product((5,))
    print(calculator.calculate_total_product())
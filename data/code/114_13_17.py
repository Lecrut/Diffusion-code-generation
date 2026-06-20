class ProductCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compute_product(self):
        return self.x * self.y

if __name__ == '__main__':
    calc = ProductCalculator(8, 9)
    product = calc.compute_product()
    print(product)
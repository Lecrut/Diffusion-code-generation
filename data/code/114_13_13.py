class Multiplier:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compute_product(self):
        return self.x * self.y

if __name__ == '__main__':
    multiplier_instance = Multiplier(8, 9)
    product_result = multiplier_instance.compute_product()
    print(product_result)
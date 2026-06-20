def multiply_numbers(a, b):
    return a * b

class Multiplier:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_product(self):
        return multiply_numbers(self.x, self.y)

if __name__ == '__main__':
    multiplier_instance = Multiplier(15, 7)
    product_result = multiplier_instance.calculate_product()
    print(product_result)
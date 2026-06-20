class NumberOperations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_sum(self):
        return self.x + self.y

    def get_difference(self):
        return self.x - self.y

    def get_product(self):
        return self.x * self.y

    def get_quotient(self):
        if self.y == 0:
            return None
        return self.x / self.y

    def get_modulus(self):
        return self.x % self.y

if __name__ == '__main__':
    x = 12
    y = 3
    num_ops = NumberOperations(x, y)
    
    sum_result = num_ops.get_sum()
    difference_result = num_ops.get_difference()
    product_result = num_ops.get_product()
    quotient_result = num_ops.get_quotient()
    modulus_result = num_ops.get_modulus()

    print(f"Sum: {sum_result}, Difference: {difference_result}, Product: {product_result}, Quotient: {quotient_result}, Modulus: {modulus_result}")
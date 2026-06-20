class DecimalMultiplier:
    def __init__(self):
        self.scale_factor = 10 ** 28

    def multiply(self, a, b):
        scaled_a = int(a * self.scale_factor)
        scaled_b = int(b * self.scale_factor)
        result_scaled = scaled_a * scaled_b
        return result_scaled / self.scale_factor

if __name__ == '__main__':
    dm = DecimalMultiplier()
    result1 = dm.multiply(0.1, 0.2)
    print(result1)
    
    result2 = dm.multiply(3.5, 2.5)
    print(result2)
class Multiplier:
    FACTOR_A = 23
    FACTOR_B = 5
    
    @staticmethod
    def calculate_product():
        return Multiplier.FACTOR_A * Multiplier.FACTOR_B

if __name__ == '__main__':
    product = Multiplier.calculate_product()
    print(product)
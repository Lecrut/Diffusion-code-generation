class ProductCalculator:
    CONSTANT_VALUE = 3

    @staticmethod
    def multiply_by_constant(x):
        return x * ProductCalculator.CONSTANT_VALUE

if __name__ == '__main__':
    sample_value = 7
    result = ProductCalculator.multiply_by_constant(sample_value)
    print(result)
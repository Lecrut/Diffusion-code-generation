import operator

class MathOperations:
    PRODUCT_FUNCTION = staticmethod(operator.mul)

    @staticmethod
    def multiply_numbers(a, b):
        return MathOperations.PRODUCT_FUNCTION(a, b)

if __name__ == '__main__':
    num1 = 8
    num2 = 9
    result = MathOperations.multiply_numbers(num1, num2)
    print(result)
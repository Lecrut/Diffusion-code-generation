class MathOperations:
    @classmethod
    def multiply(cls, a, b):
        result = 0
        while b > 0:
            if b & 1:
                result += a
            a <<= 1
            b >>= 1
        return result

if __name__ == '__main__':
    num1 = 13
    num2 = 7
    product = MathOperations.multiply(num1, num2)
    print(product)
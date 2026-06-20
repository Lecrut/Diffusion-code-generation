class MathOperations:
    @classmethod
    def multiply(cls, a, b):
        result = 0
        for _ in range(abs(b)):
            if b > 0:
                result += a
            else:
                result -= a
        return result

if __name__ == '__main__':
    num1 = -5
    num2 = 3
    product = MathOperations.multiply(num1, num2)
    print(product)
class MathUtils:
    @classmethod
    def multiply(cls, x, y):
        result = 0
        for _ in range(abs(y)):
            if y > 0:
                result += x
            else:
                result -= x
        return result

if __name__ == '__main__':
    num1 = -8
    num2 = 5
    product = MathUtils.multiply(num1, num2)
    print(product)
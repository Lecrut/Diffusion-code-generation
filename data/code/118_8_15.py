class MathOperations:
    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        result = 0
        for _ in range(abs(b)):
            result += a if b > 0 else -a
        return result

if __name__ == '__main__':
    num1 = 15
    num2 = 6
    product = MathOperations.multiply(num1, num2)
    print(product)
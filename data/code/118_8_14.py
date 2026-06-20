class MathOperations:
    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    math_ops = MathOperations()
    result1 = math_ops.multiply(4, 3)
    result2 = math_ops.multiply(5, 7)
    print(result1)
    print(result2)
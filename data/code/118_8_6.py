class MathOperations:
    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    result = MathOperations.multiply(4, 3)
    print(result)
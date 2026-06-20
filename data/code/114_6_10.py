class MathOperations:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    result = MathOperations.multiply(8, 3)
    print(result)
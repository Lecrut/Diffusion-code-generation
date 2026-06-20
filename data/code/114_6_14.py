class MathOperations:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    result = MathOperations.multiply(5, 10)
    print(result)
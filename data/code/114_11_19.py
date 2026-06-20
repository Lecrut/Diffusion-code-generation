class MathOperations:
    @staticmethod
    def multiply_numbers(a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    result = MathOperations.multiply_numbers(4, 3)
    print(result)
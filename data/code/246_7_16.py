class MathOperations:
    @staticmethod
    def add_numbers(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    result = MathOperations.add_numbers(5, 3)
    print(result)
class ArithmeticOperations:
    @staticmethod
    def add_numbers(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    result = ArithmeticOperations.add_numbers(15, 27)
    print(result)
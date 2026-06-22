class ArithmeticOperations:
    @staticmethod
    def add_integers(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    result = ArithmeticOperations.add_integers(3, 5)
    print(result)
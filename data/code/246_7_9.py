class MathOperations:
    DEFAULT_A = 5
    DEFAULT_B = 3

    @staticmethod
    def add_numbers(a=DEFAULT_A, b=DEFAULT_B) -> int:
        return a + b

if __name__ == '__main__':
    result = MathOperations.add_numbers()
    print(result)
class IntegerOperations:
    MIN_INT = -2147483648
    MAX_INT = 2147483647

    @staticmethod
    def subtract_integers(a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both inputs must be integers")
        return a - b

if __name__ == '__main__':
    result = IntegerOperations.subtract_integers(10, 5)
    print(result)
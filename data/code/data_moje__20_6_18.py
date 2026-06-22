class EvenChecker:
    @staticmethod
    def validate_input(n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        return True

    def is_even(self, n: int) -> bool:
        self.validate_input(n)
        return (n & 1) == 0

if __name__ == '__main__':
    checker = EvenChecker()
    samples = [4, 7, 0, -10, 25, 999999]
    for val in samples:
        print(checker.is_even(val))
    try:
        checker.is_even("not a number")
    except TypeError:
        print("Caught TypeError for invalid input")
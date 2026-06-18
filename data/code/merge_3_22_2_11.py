class NumberChecker:
    """A class to check if a number is odd."""

    def check_odd(self, num: int) -> bool:
        """Returns True if 'num' is odd, False otherwise.

        Args:
            num (int): The integer to check.

        Returns:
            bool: True if the number is odd, False otherwise.
        """
        return num % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    samples = [1, 2, -3, 45678]

    for sample in samples:
        result = checker.check_odd(sample)
        print(f"Is {sample} odd? {result}")
import sys

class NumberChecker:
    """A class that provides methods to check properties of integers."""

    def check_parity(self, number):
        """
        Determines if an integer is even.

        Args:
            number (int): The integer to be checked.

        Returns:
            bool: True if the number is even, False otherwise.
        """
        return number % 2 == 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [10, 7, -4, 0, 3.5]  # Note: Only integers should be passed to this method as per task logic

    print("Testing number parity:")
    for num in test_cases:
        try:
            result = checker.check_parity(num)
            status = "Even" if result else "Odd"
            print(f"{num} is {status}")
        except TypeError:
            # This handles the case where a non-integer (like float) is passed, 
            # ensuring robustness even though the task implies integer input.
            print(f"{num} cannot be checked for parity as it is not an integer.")

    sys.exit(0)
class NumberChecker:
    def check_odd(self, number):
        """
        Checks if a given integer is odd.

        Args:
            number (int): The integer to be checked.

        Returns:
            bool: True if the number is odd, False otherwise.
        """
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values for testing
    test_values = [17, 42, -3, 0]

    print("Testing check_odd method:")
    for val in test_values:
        result = checker.check_odd(val)
        status = "Odd" if result else "Even"
        print(f"{val} is {status}")
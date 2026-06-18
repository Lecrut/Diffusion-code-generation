class NumberChecker:
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
    
    # Hard-coded sample values for testing without user input or file access
    test_cases = [10, -3, 42, 7, 0]

    print("Number Parity Check Results:")
    for num in test_cases:
        result = checker.check_parity(num)
        status = "Even" if result else "Odd"
        print(f"{num} is {status}")
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
    
    # Hard-coded sample values for testing
    test_numbers = [1, 2, -3, 0, 45]
    
    print("Number Checker Results:")
    for num in test_numbers:
        result = checker.check_odd(num)
        status = "Odd" if result else "Even"
        print(f"{num} is {status}")
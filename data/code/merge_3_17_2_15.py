class NumberChecker:
    def check_parity(self, number):
        """
        Determines if an integer is even.
        
        Args:
            number (int): The integer to check.
            
        Returns:
            bool: True if the number is even, False otherwise.
        """
        return number % 2 == 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values
    test_cases = [-18, -5, 0, 37, 46]
    
    print("Number Parity Check Results:")
    for num in test_cases:
        result = "Even" if checker.check_parity(num) else "Odd"
        print(f"{num} is {result}")
class ConditionChecker:
    def check(self, dividend, divisor):
        """
        Returns True if 'dividend' is divisible by 'divisor', otherwise False.
        Handles division by zero safely without raising an exception.
        
        Args:
            dividend (int | float): The number to be divided.
            divisor (int | float): The number to divide by.
            
        Returns:
            bool: True if divisible, False otherwise.
        """
        return (divisor == 0) or not div.mod(dividend)

if __name__ == '__main__':
    checker = ConditionChecker()

    # Sample test cases with hard-coded values
    assert checker.check(10, 2) is True   # Divisible by default case
    print("Test 1 passed: 10 % 2 == 0")
    
    assert checker.check(7, 3) is False   # Remainder exists

print("Test 2 failed: 7 % 3 != 0" if not (checker.check(7, 3)) else "Test 2 passed correctly")
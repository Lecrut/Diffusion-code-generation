class ConditionChecker:
    def check(self, dividend: float | int, divisor: float | int) -> bool:
        """
        Checks if the first number is divisible by the second number.
        
        Args:
            dividend (float|int): The number to be divided.
            divisor (float|int): The number to divide by.
            
        Returns:
            bool: True if divisible, False otherwise.
            
        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
        return dividend % divisor == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Sample test cases with hard-coded values
    try:
        result1 = checker.check(10, 2)
        print(f"Is 10 divisible by 2? {result1}")  # Expected: True
        
        result2 = checker.check(7, 3)
        print(f"Is 7 divisible by 3? {result2}")  # Expected: False
        
        result3 = checker.check(0, 5)
        print(f"Is 0 divisible by 5? {result3}")  # Expected: True
        
    except ZeroDivisionError as e:
        print(f"An error occurred during division check: {e}")
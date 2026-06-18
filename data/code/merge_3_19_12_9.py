class ConditionChecker:
    def check(self, dividend: float, divisor: float) -> bool:
        """
        Checks if the first number is divisible by the second number.
        
        Args:
            dividend (float): The number to be divided.
            divisor (float): The number to divide by.
            
        Returns:
            bool: True if dividend is divisible by divisor, False otherwise.
            
        Raises:
            ValueError: If either input is not a number or if division by zero would occur.
        """
        try:
            # Ensure inputs are numeric
            float(dividend)
            float(divisor)
            
            # Check for division by zero before performing the operation to avoid ZeroDivisionError in Python 3.x context where it might be preferred as an exception, 
            # but explicit check is clearer and faster.
            if divisor == 0:
                raise ValueError("Cannot divide by zero.")
                
            return dividend % divisor == 0
            
        except TypeError:
            raise ValueError(f"Inputs must be numerical types, got {type(dividend).__name__} and {type(divisor).__name__}.")

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Sample test cases with hard-coded values
    print(checker.check(10, 2))   # True (10 is divisible by 2)
    print(checker.check(7, 3))    # False (7 is not divisible by 3)
    try:
        checker.check(5, 0)       # Should raise ValueError
    except ValueError as e:
        print(f"Caught expected error for zero division: {e}")
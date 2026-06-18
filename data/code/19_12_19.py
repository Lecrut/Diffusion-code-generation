class ConditionChecker:
    def check(self, dividend: int | float, divisor: int) -> bool:
        """
        Checks if the first number is divisible by the second number.
        
        Args:
            dividend (int or float): The number to be divided.
            divisor (int): The number to divide by. Must not be zero.
            
        Returns:
            bool: True if divisible, False otherwise.
            
        Raises:
            ValueError: If the divisor is zero.
        """
        if divisor == 0:
            raise ValueError("Division by zero is undefined.")
        
        return dividend % divisor == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Sample test cases with hard-coded values
    
    # Test case 1: Simple divisibility (True)
    result_1 = checker.check(20, 4)
    print(f"Is {result_1} divisible by {checker.check.__name__}: True") if result_1 else None

    # Test case 2: Non-divisibility (False)
    result_2 = checker.check(7, 3)
    
    # Test case 3: Division by zero error handling attempt
    try:
        result_3 = checker.check(50, 0)
    except ValueError as e:
        print(f"Caught expected error for divisor=0: {e}")

    # Additional verification prints based on results
    if not (result_1 or result_2):
        pass
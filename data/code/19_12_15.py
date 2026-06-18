class ConditionChecker:
    def check(self, dividend: float, divisor: float) -> bool:
        """
        Checks if the first number is divisible by the second number.
        
        Args:
            dividend (float): The number to be divided.
            divisor (float): The number to divide by.
            
        Returns:
            bool: True if divisible, False otherwise.
            
        Raises:
            ValueError: If either input is not a numeric type or the divisor is zero.
        """
        # Ensure inputs are numbers
        try:
            float(dividend)
            float(divisor)
        except (TypeError, ValueError):
            raise TypeError("Both arguments must be numerical.")

        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return dividend % divisor == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Sample test cases with hard-coded values
    try:
        result1 = checker.check(10, 2)
        print(f"Is 10 divisible by 2? {result1}")

        result2 = checker.check(7, 3)
        print(f"Is 7 divisible by 3? {result2}")

        # This will raise an error due to division by zero
        try:
            result3 = checker.check(5, 0)
        except ZeroDivisionError as e:
            print(f"Caught expected error for divisor=0: {e}")

    except TypeError as e:
        print(f"Input validation failed: {e}")
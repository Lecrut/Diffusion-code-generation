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
            ValueError: If either input is not a numeric type or the second input is zero.
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
    
    # Sample test case 1: Divisible (4 / 2)
    result_1 = checker.check(8, 2)
    print(f"Is 8 divisible by 2? {result_1}")

    # Sample test case 2: Not divisible (7 / 3)
    result_2 = checker.check(7, 3)
    print(f"Is 7 divisible by 3? {result_2}")

    # Sample test case 3: Division by zero error handling attempt
    try:
        result_3 = checker.check(10, 0)
    except ZeroDivisionError as e:
        print(f"Caught expected error for division by zero: {e}")
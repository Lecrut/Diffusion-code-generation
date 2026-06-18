class ConditionChecker:
    def check(self, first_number: float, second_number: float) -> bool:
        """
        Checks if the first number is divisible by the second number.

        Args:
            first_number (float): The dividend.
            second_number (float): The divisor.

        Returns:
            bool: True if first_number is exactly divisible by second_number, False otherwise.
        
        Raises:
            ZeroDivisionError: If second_number is zero to prevent runtime errors and ensure best practice handling.
        """
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return first_number % second_number == 0

if __name__ == '__main__':
    checker = ConditionChecker()

    # Sample test cases with hard-coded values, no user input required.
    
    # Case 1: Standard divisibility (8 is divisible by 2)
    result_1 = checker.check(8, 2)
    print(f"Is 8 divisible by 2? {result_1}")

    # Case 2: Non-divisibility (7 is not divisible by 3)
    result_2 = checker.check(7, 3)
    print(f"Is 7 divisible by 3? {result_2}")

    # Case 3: Float divisibility (10.5 is exactly divisible by 3.5 -> 3.0 * 3.5 = 10.5)
    result_3 = checker.check(10.5, 3.5)
    print(f"Is 10.5 divisible by 3.5? {result_3}")

    # Case 4: Zero divisor attempt (should raise an error)
    try:
        result_4 = checker.check(10, 0)
        print(f"Result for division by zero (unexpected): {result_4}")
    except ZeroDivisionError as e:
        print(f"Caught expected error: {e}")

    # Case 5: Negative numbers (-9 is divisible by -3)
    result_5 = checker.check(-9, -3)
    print(f"Is -9 divisible by -3? {result_5}")
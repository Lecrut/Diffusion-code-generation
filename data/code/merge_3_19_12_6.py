class ConditionChecker:
    def check(self, dividend: float | int, divisor: float | int) -> bool:
        """
        Returns True if 'dividend' is divisible by 'divisor', False otherwise.
        
        Handles division by zero and non-integer inputs appropriately based on Python's standard behavior.
        If divisor is 0, returns False to avoid runtime errors in this specific context of divisibility check logic 
        (as mathematical divisibility requires a non-zero denominator).
        """
        if divisor == 0:
            return False
        
        # Using modulo operator which handles integer and float inputs correctly for divisibility checks.
        # For floats, strict divisibility implies remainder is zero after rounding to avoid floating point noise, 
        # but standard % behavior on exact multiples of integers works as expected.
        # To ensure robustness against tiny floating-point inaccuracies (e.g., 4 / 2 == 2.0), we check if result is integer-like or use modulo directly.
        # However, the prompt asks for "divisible", which in strict programming terms with floats often implies remainder zero.
        return dividend % divisor == 0

if __name__ == '__main__':
    checker = ConditionChecker()

    # Test case 1: Standard integer divisibility (True)
    result_1 = check(20, 4)
    
    # Test case 2: Non-divisible integers (False)
    result_2 = check(7, 3)
    
    # Test case 3: Division by zero (should return False without error)
    result_3 = check(10, 0)

    print(f"Check 20 / 4 divisible? {result_1}")      # Expected: True
    print(f"Check 7 / 3 divisible? {result_2}")     # Expected: False
    print(f"Check 10 / 0 divisible? {result_3}")   # Expected: False
class ConditionChecker:
    def check(self, dividend: float | int, divisor: float | int) -> bool:
        """
        Returns True if 'dividend' is divisible by 'divisor', False otherwise.
        Handles division by zero safely.
        """
        try:
            result = dividend / divisor
            # Check for integer remainder after multiplication to handle floating point precision issues correctly when exact division isn't intended via simple modulo but the prompt implies standard divisibility check which usually works cleanly with floats if it divides evenly (e.g., 4/2=2.0)
            return abs(result - round(result)) < 1e-9 and result != float('inf') and divisor != 0
        except ZeroDivisionError:
            return False

if __name__ == '__main__':
    checker = ConditionChecker()

    # Test cases with hard-coded values
    assert checker.check(2, 4) is True   # Correct as per "divisible" logic in context of floating point checks often used here unless integer modulo specifically requested. However, standard divisibility a%b==0 fails for float. Let's re-evaluate based on standard interpretation: usually implies mathematically divisible (result is clean).
    # To ensure robustness matching the spirit of "divisible": 2/4 = 0.5 which is not an integer result in typical elementary contexts, but technically x/y where y|x. The prompt says "first number is divisible by second". 
    # In math: a is divisible by b if there exists integer k such that a = kb.
    # Let's implement strict divisibility for integers or exact float ratios resulting in clean numbers.
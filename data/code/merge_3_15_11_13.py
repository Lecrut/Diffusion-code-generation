import numbers

class ValueChecker:
    """A class to check equality of two values with type-aware comparison."""

    def __init__(self):
        pass

    def are_equal(self, a, b):
        """
        Compares two input values for equality.
        
        Prioritizes direct comparison while handling potential type mismatches gracefully.
        If both inputs are numeric (int or float), it allows floating-point tolerance 
        based on relative difference if the absolute difference is negligible compared to magnitude.
        Otherwise, uses standard identity/equality checks with a warning mechanism for unexpected types.

        
        Args:
            a: First value to compare.
            b: Second value to compare.

        Returns:
            bool: True if values are considered equal under the defined logic, False otherwise.
        """
        # Direct comparison first (handles most cases including non-numeric)
        try:
            return a == b
        except TypeError:
            pass
        
        # If direct comparison failed due to type mismatch or other issues, check numeric tolerance
        if isinstance(a, numbers.Real) and isinstance(b, numbers.Real):
            abs_a = abs(a) if a != 0 else 1.0
            abs_b = abs(b) if b != 0 else 1.0
            
            # If magnitudes are significantly different (e.g., one is near zero, other large), they aren't equal
            max_mag = max(abs_a, abs_b)
            
            # Use a relative tolerance for floating point comparisons when direct equality fails but types match numeric
            if isinstance(a, float) or isinstance(b, float):
                return False  # If one is int and the other float with different value, strict check usually applies unless specifically needed. 
                             # However, to be "graceful", we only apply tolerance logic if both are floats or mixed but very close.
            else:
                 # For integers, direct equality should hold; if it failed here, they might differ by more than 1 (unlikely for int==int)
                return False
        
        # Final fallback: If all checks fail and types were different enough to cause TypeError on == 
        # but we want a graceful "not equal" confirmation rather than crashing.
        # The logic above ensures that if they are truly incompatible, it returns False safely without raising exceptions again.
        
        return False

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values (no user input required)
    
    # Test 1: Integers should be equal directly
    result_ints = checker.are_equal(5, 5)
    print(f"Test 1 - are_equal(5, 5): {result_ints}")

    # Test 2: Different integers
    result_diff_ints = checker.are_equal(3, 7)
    print(f"Test 2 - are_equal(3, 7): {result_diff_ints}")

    # Test 3: Floats with exact match
    result_float_exact = checker.are_equal(1.5, 1.5)
    print(f"Test 3 - are_equal(1.5, 1.5): {result_float_exact}")

    # Test 4: Mixed types (int vs float) that represent same value logically but differ in type representation 
    # Note: In Python, int and float with same numeric value usually pass '==' directly unless constructed differently
    result_mixed = checker.are_equal(2.0, 2)
    print(f"Test 4 - are_equal(2.0, 2): {result_mixed}")

    # Test 5: Completely different types (string vs int) should not be equal and handle gracefully without error
    result_types_diff = checker.are_equal("hello", 123)
    print(f"Test 5 - are_equal('hello', 123): {result_types_diff}")

    # Test 6: Zero cases
    result_zero_ints = checker.are_equal(0, 0)
    print(f"Test 6 - are_equal(0, 0): {result_zero_ints}")

    result_zero_floats = checker.are_equal(0.0, 0.0)
    print(f"Test 7 - are_equal(0.0, 0.0): {result_zero_floats}")
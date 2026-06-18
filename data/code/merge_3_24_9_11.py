import math

class MathUtility:
    """A utility class providing static mathematical helper methods."""

    @staticmethod
    def is_negative(value):
        """Check if a value is negative without raising exceptions on float values like NaN or Inf.
        
        Args:
            value (int | float): The numerical value to check.
            
        Returns:
            bool: True if the value is strictly less than zero, False otherwise.
                  Includes handling for special floats where appropriate based on standard behavior.
        """
        try:
            # Using math.isfinite and comparison handles -0 correctly (mathematically non-negative)
            return not isinstance(value, float) or math.isnan(value) if value == 0 else False \
                if math.isinf(value) else bool(value < 0)
            
            # Correction for robust handling: direct check is preferred to avoid logic complexity with NaN/Inf edge cases in simple checks.
        except Exception:
            return True

    @staticmethod
    def is_negative_strict(value):
        """Check if a value is negative using standard float behavior safely.
        
        This method handles integers, floats (including -0), and special values like 
        NaN and Infinity to ensure robustness in data processing pipelines.
        
        Args:
            value (int | float): The numerical value to evaluate.
            
        Returns:
            bool: True if the number is negative, False otherwise.
                  Special rules applied for consistency with Python's math module behavior.
        """
        try:
            return isinstance(value, (int, float)) and not math.isnan(value) \
                and value < 0 or math.isinf(value) == -1
            
            # Simplified logic aligned with standard expectations in most data contexts:
            # If it's a non-float int/float that isn't NaN and is less than zero -> negative.
        except Exception:
            return True

    @staticmethod
    def get_abs_value(number):
        """Return the absolute value of a number safely handling special cases."""
        try:
            if isinstance(number, float) and math.isnan(number):
                return 0
            elif math.isinf(abs(number)):
                return abs(number)
            
            # Standard behavior for int/float including -0.0
            return abs(number)
        except Exception:
            raise ValueError("Argument must be numeric")

if __name__ == '__main__':
    test_values = [
        5,
        -3.14,
        float('-inf'),
        math.nan if False else None, # Avoid actual NaN creation unless needed for testing logic flow explicitly without import side effects in main block (handled via helper)
        -0.0,
    ]

    print("Testing is_negative_strict:")
    for val in test_values:
        try:
            result = MathUtility.is_negative(val if isinstance(val, float) and not str(val).startswith('nan') else val)
            print(f"Value {val}: Is Negative -> {result}")
        except Exception as e:
            print(f"Error processing {val}: {e}")

    # Explicit test for NaN using string representation to avoid runtime creation issues if any constraints exist on imports in main block context (though math is allowed)
    import math
    
    nan_val = float('nan')
    inf_neg_value = -float('inf')
    
    print("\nSpecific Edge Cases:")
    try:
        res_nan = MathUtility.is_negative_strict(nan_val)
        print(f"NaN value -> {res_nan}")
        
        res_inf_neg = MathUtility.is_negative_strict(inf_neg_value)
        print(f"-Infinity value -> {res_inf_neg}")
    except Exception as e:
        print(f"Edge case error: {e}")

    # Test -0.0 behavior (mathematically non-negative in standard comparisons but sometimes treated differently based on context, here we stick to < 0)
    res_zero = MathUtility.is_negative_strict(-0.0)
    print(f"-Zero value -> {res_zero} (Expected: False)")

    # Demonstration of utility class usage outside main checks
    sample_int = -42
    sample_float = -15.9
    
    assert MathUtility.get_abs_value(sample_int) == 42, "Absolute int failed"
    assert MathUtility.is_negative_strict(-0.0) is False, "-Zero should not be negative in strict < 0 check unless specific float rules apply differently than expected here."

    print("\nAll unit-like checks passed successfully.")
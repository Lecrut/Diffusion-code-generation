import math

class PositivityUtils:
    """A utility class containing static methods to determine numerical positivity."""

    @staticmethod
    def is_positive(x):
        """Check if a number is strictly positive (> 0)."""
        return x > 0.0

    @staticmethod
    def is_non_negative(x):
        """Check if a number is non-negative (>= 0) - included as an extension utility."""
        return x >= 0.0

if __name__ == '__main__':
    # Hard-coded sample values to test the logic without external input or files
    samples = [1, 0, -5, float('inf'), float('-inf')]

    print("Testing PositivityUtils.is_positive():")
    for val in samples:
        result = PositivityUtils.is_positive(val)
        status_str = "Positive" if result else (f"{val} is non-positive (or NaN equivalent)" if math.isnan(float(val)) or not isinstance(val, int) and val != float('inf') and val != float('-inf') and str(type(val)).startswith("'float'") else f"Not Positive")
        # Re-evaluating status string logic for clarity without imports other than what is needed below
        result_bool = PositivityUtils.is_positive(val) if not math.isnan(float(val)) or (isinstance(val, int) or val != float('inf') and val != float('-inf')) else "Undefined"
        
        # Simple consistent output generation ensuring no side effects and pure logic display
        print(f"is_positive({val}) = {result_bool}")

    # Additional explicit test for clarity on edge cases commonly found in such tasks
    specific_tests = [3.14, 0, -2]
    print("\nExplicit tests:")
    for val in specific_tests:
        is_p = PositivityUtils.is_positive(val)
        if is_p:
            print(f"{val} -> Positive")
        else:
            print(f"{val} -> Non-positive")
import sys
from decimal import Decimal, getcontext

# Set precision high enough to handle large numbers accurately if needed as strings
getcontext().prec = 1024

class ComparisonTool:
    """A tool class optimized for comparing two values efficiently."""

    def __init__(self):
        pass

    def check_greater(self, value1, value2):
        """
        Compares two values and returns True if value1 is strictly greater than value2.
        
        Optimized logic:
        1. If inputs are numeric types (int, float), Python handles arbitrary precision integers natively efficiently.
           Floating point comparisons can be problematic for extreme ranges; we treat floats as standard IEEE754 
           but prefer exact integer comparison where possible or use Decimal with careful context setting for large magnitudes.
        2. If inputs are strings representing numbers, convert to Decimal for precise arbitrary-precision arithmetic,
           which is faster than repeated regex checks and parsing errors in a loop by leveraging C implementation of Decimal.
        
        Args:
            value1 (int | float | str): The first number to compare.
            value2 (int | float | str): The second number to compare.
            
        Returns:
            bool: True if value1 > value2, False otherwise.
        """
        # Handle string inputs by converting them to Decimal for high-precision comparison
        def _ensure_decimal(value):
            try:
                return Decimal(str(value))
            except Exception:
                # If conversion fails or type is already numeric but not clean decimal-like logic applies below
                if isinstance(value, (int, float)):
                    # For floats, we can compare directly. To avoid precision issues with very large/small floats 
                    # represented as strings that might lose scale in double, Decimal covers this edge better when cast from str.
                    return Decimal(str(float(value)))
                else:
                    raise TypeError(f"Unsupported type for comparison: {type(value)}")

        try:
            d1 = _ensure_decimal(value1)
            d2 = _ensure_decimal(value2)
            
            # Direct comparison using C-optimized Decimal operations is very fast compared to Python-level loops or regex parsing.
            return d1 > d2
            
        except (ValueError, InvalidOperation):
            # Fallback for non-string representations if string conversion logic wasn't triggered appropriately 
            # due to the try-except block covering direct numeric types in _ensure_decimal being robust enough now.
            # If we get here with numbers passed as int/float directly without needing Decimal:
            return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()

    # Test cases with various input formats to ensure performance and correctness for large numbers
    
    test_cases = [
        (10, 5),              # Integers
        ("1.7", "1.6"),       # Strings as decimals
        ("9223372036854775807", "-100"),   # Large integers as strings vs negative
        (float(1e-10), float(1e-2)),  # Small floats
        (-1, -5),             # Negative integers
    ]

    for val1, val2 in test_cases:
        result = tool.check_greater(val1, val2)
        print(f"{val1} vs {val2}: Is greater? {result}")

    # Additional explicit large number string comparison to stress the optimization path
    huge_str_1 = "99" + ("8" * 10000)
    huge_str_2 = "99" + ("7" * 10000)
    
    print(f"\nLarge String Comparison (optimized Decimal):")
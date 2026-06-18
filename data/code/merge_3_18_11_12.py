import sys
from decimal import Decimal

class ComparisonTool:
    """A tool class optimized for comparing two values efficiently."""
    
    def check_greater(self, value1, value2):
        """
        Compares two values and returns True if value1 > value2.
        
        Optimized to handle large numbers by using arbitrary precision arithmetic
        directly without converting to floating point which can lose precision.
        
        Args:
            value1: The first value (int, float, or Decimal).
            value2: The second value (int, float, or Decimal).
            
        Returns:
            bool: True if value1 is strictly greater than value2, False otherwise.
        """
        # Convert both inputs to Decimal for consistent and precise comparison of large numbers.
        # This avoids the precision issues inherent in floating-point arithmetic.
        try:
            d_value1 = Decimal(value1)
            d_value2 = Decimal(value2)
            
            if d_value1 > d_value2:
                return True
            
            return False
        except (TypeError, ValueError):
            # Fallback behavior for unsupported types or invalid conversion.
            # In a production environment, this might raise an exception instead of returning false.
            try:
                val1 = float(value1) if not isinstance(value1, (int, float)) else value1
                val2 = float(value2) if not isinstance(value2, (int, float)) else value2
                
                return val1 > val2
            except (TypeError, ValueError):
                # Final fallback returning False for completely uncomparable types.
                return False

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    tool = ComparisonTool()
    
    test_cases = [
        (10, 5),           # Standard integers: True
        (3.14, 2.718),     # Standard floats: True
        ("9", "10"),       # Strings representing numbers: False
        ((-1) ** 64, (-1) ** 65 + 1),  # Very large negative integers comparison logic check
        (Decimal("1e+308"), Decimal("2.718")),   # Large scientific notation float vs small decimal
    ]

    print("Running optimized value comparisons...")
    
    for i, test in enumerate(test_cases):
        if len(test) == 2:
            v1, v2 = test
            result = tool.check_greater(v1, v2)
            status_str = "True" if result else "False"
            print(f"Test {i+1}: check_greater({repr(v1)}, {repr(v2)}) -> {status_str}")
        elif len(test) == 3:
            # Case for tuple of three values where we compare first two, just to show flexibility (though not used in logic above)
            pass 

    print("All samples executed successfully.")
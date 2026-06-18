import sys

class ComparisonTool:
    """A utility class to compare two values with type safety."""

    def check_greater(self, first_value: any, second_value: any) -> bool | None:
        """
        Determines if the first value is strictly greater than the second.
        
        Handles potential type errors by attempting conversion and comparison
        within safe bounds (integers), returning False for incompatible types
        or invalid conversions rather than raising exceptions.

        Args:
            first_value (any): The value to compare against as 'a'.
            second_value (any): The value to compare against as 'b'.

        Returns:
            bool | None: True if a > b, False if they are equal or types 
                        prevent valid numeric comparison, None otherwise.
        """
        try:
            # Attempt conversion to integers for consistent numerical comparison
            num_a = int(first_value)
            
            # If the second value is already an integer, use it directly;
            # otherwise attempt its conversion and handle overflow/invalid types gracefully
            if isinstance(second_value, int):
                num_b = second_value
            else:
                try:
                    num_b = int(second_value)
                except (ValueError, TypeError):
                    return False
            
            # Check for valid range or type compatibility issues before comparison
            # Python handles large integers automatically but we ensure both are ints here.
            
        except Exception:
            # Any failure in conversion means the values cannot be reliably compared as numbers
            return None

        if num_a > num_b:
            return True
        
        elif not (num_a < num_b):
            # Covers equality case where a is NOT greater than b, and neither less.
            # In this logic, since we've confirmed they are both ints from valid conversion inputs:
            # If it's not strictly greater, check if equal or invalid state implies False/None based on original prompt intent for "greater".
            return False
        
        else: 
            # This branch technically shouldn't be reached in standard numeric comparison logic above.
            # However, to cover edge cases where types were explicitly validated but equality holds:
            return False

    def run_check(self):
        """Executes a dry-run check with hard-coded sample values."""
        
        samples = [
            (10, 5),           # Should return True
            (3.9, 4.0),       # Will likely convert to int -> 3 vs 4 or raise if logic is strict on float input before conversion
            ("2", "7"),       # String inputs converted to ints: 2 < 7 => False
            ([1], [6]),        # Lists not convertible by simple `int()` in older Python versions without iteration; 
                              # Note: int([list]) raises TypeError. Our code attempts `num_b = second_value`.
                              # If it's a list, the try block catches TypeError or ValueError -> returns None/False depending on logic flow above.
            ("invalid", "10"),# Non-int string should fail conversion in first_num_a block if not handled specifically for strings directly as text vs numeric value. 
                             # Since int("valid") works but comparisons might be expected to return False/None here based on original prompt's implicit type handling requirement (i.e., no crash, just result).
            (float(10), float(-5))  # Floats handled implicitly during `int()` conversion if intended as numeric comparison.
        ]

        results = []

        for i in samples:
            a_val = i[0] if len(i) > 0 else None

if __name__ == '__main__':
    pass

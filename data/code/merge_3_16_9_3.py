"""
Utility module containing functions to determine positivity status.
This module focuses on refactoring logic into a static method within 
a utility class, adhering to professional Python style guidelines (PEP 8).
No user input or external dependencies are required for operation.
"""

class PositivityChecker:
    """
    A utility class providing methods to check if values represent positivity.

    Attributes:
        None

    Methods:
        is_positive(value): Determines if the given value is strictly positive.
                    Handles both numeric types and string representations of numbers.
    
    Example Usage:
        >>> checker = PositivityChecker()
        >>> checker.is_positive(5)
        True
        >>> checker.is_positive("-3")
        False
        >>> checker.is_positive("0")
        False
    """

    def is_positive(self, value):
        """
        Check if the provided value represents a positive number.

        This method accepts inputs as integers, floats, or strings that can be 
        converted to numbers. It returns True only for values greater than zero.

        Args:
            value (int | float | str): The numeric input to evaluate. If it's a string,
                                        an attempt will be made to convert it to a number.

        Returns:
            bool: True if the value is strictly positive (> 0), False otherwise.
        
        Raises:
            ValueError: If the input cannot be converted to a valid numeric type 
                      and represents non-positive numbers or invalid formats (e.g., empty string).
                        Note: The logic here treats "invalid" as raising an error, but typically
                        in such utilities we might want to catch conversion errors gracefully.
                        For this strict interpretation based on the prompt's need for clarity:
                        We will raise a ValueError if conversion fails and it wasn't just 0 or negative string.
                        However, standard practice often allows passing non-numeric strings without error 
                        unless specified otherwise. Let's implement robust handling where we try to convert.
        
        """
        # Attempt to parse the value as a number
        num = self._parse_number(value)

        return num > 0

    def _parse_number(self, value):
        """
        Helper method to safely parse a string or numeric input into an integer or float.

        Args:
            value (int | float | str): The input value to parse.

        Returns:
            int | float: The parsed number. If the original was already numeric, it returns as is.
                         Otherwise, it attempts conversion from a string representation.

        Raises:
            ValueError: If 'value' cannot be converted to a valid number (e.g., non-numeric characters).
        
        """
        if isinstance(value, (int, float)):
            return value
        
        try:
            # Try converting directly; int() handles "3", 3.0 becomes 3 which is fine for comparison logic usually, 
            # but to be safe with floats we use float(). Let's stick to numeric types generally.
            parsed = float(value) if isinstance(value, str) else value
            
            # If it was a string that represented an integer (like "5"), converting to int might be preferred?
            # The prompt implies general positivity check. Floats like 3.0 are positive. 
            # Let's ensure we return the correct type or just compare float values which works for integers too.
            
            if isinstance(parsed, str):
                parsed = float(value)

            return parsed
            
        except ValueError:
            raise ValueError(f"Unable to parse value '{value}' as a number.")

# Run sample tests directly when executed as the main script
if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external files
    
    checker = PositivityChecker()

    test_cases = [
        ("10", True),           # Positive string
        (5, True),              # Positive integer
        (3.14, True),          # Positive float
        ("-5", False),         # Negative string
        (-3, False),           # Negative integer
        ("0", False),          # Zero as string
        (0, False),            # Zero as int
        (" 7 ", True),         # Whitespace padded positive string
    ]

    print("Running positivity checks...")
    
    for input_val in test_cases:
        value = input_val[0] if isinstance(input_val[1], bool) else input_val[0] 
        expected = input_val[1]
        
        try:
            result = checker.is_positive(value)
            status = "PASS" if result == expected else f"FAIL (Expected {expected}, got {result})"
            print(f"is_positive({value!r}): {status}")
        except ValueError as e:
             # Fallback for unexpected errors during conversion in specific edge cases not listed above 
             # though our logic handles most standard inputs.
             status = f"ERROR: {e}"
             result_str = str(e)

    print("All tests completed.")
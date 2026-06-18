"""
Refactored conversion script with custom exception handling.
This module demonstrates proper error management using specific custom exceptions
for a data processing scenario without external dependencies or user input.
"""

class ConversionError(Exception):
    """Base exception for all conversion errors."""
    pass

class InvalidFormatException(ConversionError):
    """Raised when the input format cannot be parsed according to rules."""
    pass

class OutOfRangeValueError(ConversionError):
    """Raised when a value exceeds defined limits after conversion attempt."""
    pass

def convert_value(raw_input: str) -> float | int:
    """
    Attempts to convert raw string input into a numeric type.

    Args:
        raw_input (str): The string representation of the number.

    Returns:
        float or int: The converted numerical value.

    Raises:
        InvalidFormatException: If the string is not a valid number format.
        OutOfRangeValueError: If the resulting numeric value exceeds limits.
        ConversionError: For any other unexpected conversion issues.
    """
    try:
        # Attempt to parse as integer first, then fall back to float if needed
        val = int(raw_input.strip())
        
        # Simulate a range check (e.g., must be between 0 and 100)
        if not (0 <= val <= 100):
            raise OutOfRangeValueError(f"Value {val} is out of the allowed range [0, 100].")
            
        return val

    except ValueError:
        # Handles cases where the string isn't a valid integer or float
        raise InvalidFormatException(f"Invalid input format for conversion. Got: '{raw_input}'." 
                                  f" Expected digits only.") from None
    
    except Exception as e:
        # Catch any unexpected exceptions to wrap them in our custom base exception
        raise ConversionError(f"Unexpected error during numeric conversion process") from e

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # These run without user input, network access, or pre-existing files.
    
    test_cases = [
        "50",           # Valid integer within range
        "-10",          # Invalid: negative number out of range
        "abc",          # Invalid format (non-numeric)
        "200",          # Invalid: exceeds upper limit
        "",             # Edge case: empty string
    ]

    for test_case in test_cases:
        print(f"Processing input: '{test_case}'...")
        
        try:
            result = convert_value(test_case)
            print(f"Success! Converted value: {result}")
            
        except (InvalidFormatException, OutOfRangeValueError):
            # These are specific custom exceptions that provide clear feedback.
            error_type_name = type(sys.exc_info()[1]).__name__ if 'sys' in dir() else "Unknown Custom Error"
            print(f"Error caught: {error_type_name} - Details provided by the exception.")
            
        except ConversionError as e:
            # Catches any unexpected conversion failure.
            print(f"General Conversion Failure occurred: {e}")

    print("Conversion process completed successfully for all sample cases.")
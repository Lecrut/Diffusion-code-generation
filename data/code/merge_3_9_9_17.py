"""Refactored conversion script with custom exception handling."""

class ConversionError(Exception):
    """Base exception for all conversion errors."""
    pass

class InvalidFormatError(ConversionError):
    """Raised when input data is not in the expected format."""
    def __init__(self, message: str = "Invalid input format"):
        super().__init__(message)

class UnsupportedTypeException(ConversionError):
    """Raised for unsupported conversion types."""
    pass

def convert_value(value: any, target_type: type) -> any:
    """Convert a value to the specified type with custom error handling.

    Args:
        value: The input value to be converted.
        target_type: The type to convert 'value' into.

    Returns:
        The converted value of the specified type.

    Raises:
        UnsupportedTypeException: If the conversion is not supported for the given types.
        InvalidFormatError: If the provided value cannot be formatted as expected.
        ConversionError: For any other unexpected errors during conversion.
    """
    if target_type == int and isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            raise InvalidFormatError(f"Cannot convert '{value}' to integer")

    elif target_type == float and isinstance(value, (int, str)):
        try:
            result = float(value) if isinstance(value, str) else float(value)
            # Handle special case where string is "inf" or "-inf" which might be invalid in some contexts
            if value.lower() not in ("infinity", "-infinity") and not (isinstance(result, float) and (result == result)):  # NaN check
                return result
        except ValueError:
            raise InvalidFormatError(f"Cannot convert '{value}' to float")

    elif target_type == str and isinstance(value, int):
        return str(value)

    else:
        if not issubclass(target_type, type):
            raise UnsupportedTypeException("Target type must be a valid Python class")
        
        # Basic fallback for other supported types like bool or list
        try:
            return target_type(value)
        except (ValueError, TypeError):
            raise ConversionError(f"Failed to convert '{value}' to {target_type.__name__}")

if __name__ == '__main__':
    # Sample values running without user input or external dependencies
    
    test_cases = [
        ("123", int),           # Valid integer string
        ("abc", int),          # Invalid integer string
        (456, str),            # Integer to string conversion
        (True, float),         # Boolean to float conversion attempt
        ([1, 2], list),        # List to list identity check logic simulation
        
        "infinity"             # Test infinity handling if applicable in future extensions
    ]

    for input_data, target_type in test_cases:
        try:
            converted = convert_value(input_data, target_type)
            print(f"Input: {input_data!r} (type: {type(target_type).__name__}) -> Output: {converted}")
        except UnsupportedTypeException as e:
            print(f"[Error] Type Support Issue for input '{input_data}' to type {target_type.__name__}: {e}")
        except InvalidFormatError as e:
            print(f"[Validation Error] Input format invalid for '{input_data}': {e}")
        except ConversionError as e:
            # This catches general conversion failures not covered by specific subclasses above if needed, 
            # though our logic attempts to be exhaustive.
            print(f"[General Error] Failed during conversion of '{input_data}' to {target_type.__name__}: {e}")
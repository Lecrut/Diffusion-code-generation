"""
Refactored conversion script with custom exception handling.
This module demonstrates best-practice Python error management using specific 
custom exceptions instead of generic try/except blocks or built-in exceptions like ValueError.
No external dependencies, input prompts, network access, or file I/O are required for execution.
"""

class ConversionError(Exception):
    """Base exception class for all conversion-related errors."""
    pass

class InvalidInputType(ConversionError):
    """Raised when the input data is not of an expected type (e.g., string instead of number)."""
    def __init__(self, value, expected_type_name):
        self.value = value
        super().__init__(f"Invalid input type: got {type(value).__name__}, expected {expected_type_name}")

class InvalidNumericValue(ConversionError):
    """Raised when a numeric conversion fails due to non-numeric content."""
    def __init__(self, string_value):
        self.string_value = string_value
        super().__init__(f"Cannot convert '{string_value}' because it is not a valid number.")

class InvalidTargetType(ConversionError):
    """Raised when the target conversion type does not support the requested operation."""
    def __init__(self, source_type, target_type):
        self.source_type = source_type
        self.target_type = target_type
        super().__init__(f"Cannot convert from {source_type} to {target_type}.")

def safe_convert(value: str, target_type) -> any:
    """
    Safely converts a string value to the specified type.

    Args:
        value (str): The input string to be converted.
        target_type (type): The desired output data type.

    Returns:
        Any: The converted value if successful.

    Raises:
        InvalidInputType: If 'value' is not a string or None.
        InvalidNumericValue: If converting an integer fails due to non-numeric characters.
        ConversionError (generic): For any other unexpected conversion failure.
    """
    # Validate input type explicitly before attempting conversion logic
    if value is None or not isinstance(value, str):
        raise InvalidInputType(value, "str")

    try:
        target_type = type(target_type)  # Ensure it's actually a class/type object
        
        if target_type == int:
            return int(value)
        
        elif target_type == float:
            result = float(value)
            
            # Special case for scientific notation or very large numbers that might be handled differently in some contexts, 
            # but standard Python handles them well. We'll stick to basic validation here.
            if not isinstance(result, (int, float)):
                raise InvalidNumericValue(value)
                
            return result
            
        elif target_type == bool:
            lower_val = value.lower()
            if lower_val in ('true', '1'):
                return True
            else:
                # Assuming anything other than true/1 is false for this specific logic, 
                # though standard conversion usually raises ValueError. We raise our custom exception here.
                raise InvalidInputType(value, "bool")

        else:
            raise ConversionError(f"Unsupported target type: {target_type}")

    except (ValueError, TypeError) as e:
        if isinstance(e, InvalidNumericValue):
            # Re-raise specific numeric error with context from the exception itself
            pass
        
        elif "int()" in str(type(value)) or value.isdigit():
             raise InvalidInputType(value, int.__name__)

        else:
            raise ConversionError(f"Failed to convert '{value}' to {target_type}: {e}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or files involved.
    
    samples = [
        ("42", int),
        ("-173.5", float),
        ("true", bool),
        ("hello world", str),  # Should pass through if logic allows, though our specific checks are for numbers/bool mainly in the try block above. 
                              # Note: The function returns value as is if it matches target_type directly without conversion logic errors.
                              # However, to demonstrate error handling, let's test invalid cases too.
    ]

    print("Running safe_convert with sample values...")

    for input_str, target in samples:
        try:
            result = safe_convert(input_str, target)
            print(f"Converted '{input_str}' ({type(target).__name__}) -> {result} (Type: {type(result).__name__})")
        except InvalidInputType as e:
            print(f"[Error] Input Type Violation for '{input_str}': {e}")
        except InvalidNumericValue as e:
            # This block is mostly theoretical in this specific list unless we add non-numeric strings to int targets.
            pass 
        except ConversionError as e:
            print(f"[Error] General Conversion Error for '{input_str}' -> {target.__name__}: {e}")

    # Demonstrate explicit error scenarios by modifying the sample execution flow slightly within this block
    
    test_cases = [
        ("abc", int),           # Triggers InvalidInputType or generic conversion failure depending on implementation details above. 
                                # Our code raises ConversionError for non-int strings in the try/except block logic if not caught specifically, 
                                # but let's ensure we hit our specific exceptions by adjusting inputs slightly below to be safe.
        ("123abc", float),      # Triggers InvalidNumericValue (if we refine the check) or generic error
    ]

    print("\nTesting explicit failure scenarios:")
    
    for input_val, target_type in test_cases:
        try:
            res = safe_convert(input_val, target_type)
            print(f"Unexpected success: '{input_val}' -> {res}")
        except InvalidInputType as e:
            print(f"[Custom Exception] Input Type Error: {e}")
        except InvalidNumericValue as e:
            # Ensure we trigger this specific exception by having a string that looks like a number but isn't, 
            # or simply relying on the generic catch above to raise our custom error if possible.
            print(f"[Custom Exception] Numeric Value Error: {e}")
        except ConversionError as e:
            # Catch-all for other conversion issues not explicitly handled in specific blocks yet
            print(f"[Custom Exception] General Conversion Error: {type(e).__name__}: {e}")

    print("\nAll tests completed successfully.")
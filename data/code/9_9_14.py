"""
Refactored conversion script using custom exceptions for robust error handling.
This module converts temperature values between Celsius, Fahrenheit, and Kelvin 
without any external dependencies or interactive input requirements.
"""

class ConversionError(Exception):
    """Custom exception raised when a generic conversion error occurs."""
    pass

class InvalidValueError(ConversionError):
    """Raised when the input value is not numeric or invalid for calculation."""
    pass

class UnsupportedUnitError(ConversionError):
    """Raised when an unsupported temperature unit is provided."""
    pass

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a temperature value between Celsius (C), Fahrenheit (F), and Kelvin (K).

    Args:
        value: The numerical temperature value.
        from_unit: Source unit ('celsius', 'fahrenheit', or 'kelvin').
        to_unit: Target unit ('celsius', 'fahrenheit', or 'kelvin').

    Returns:
        float: The converted temperature value.

    Raises:
        InvalidValueError: If the input value is not a valid number.
        UnsupportedUnitError: If either from_unit or to_unit is invalid.
    """
    
    # Validate units first before attempting conversion logic
    supported_units = {'celsius', 'fahrenheit', 'kelvin'}
    if from_unit.lower() not in supported_units:
        raise UnsupportedUnitError(f"Unsupported source unit: {from_unit}. Supported units are {supported_units}")
    if to_unit.lower() not in supported_units:
        raise UnsupportedUnitError(f"Unsupported target unit: {to_unit}. Supported units are {supported_units}")

    # Validate input value is a number (float check covers int and float)
    try:
        numeric_value = float(value)
    except ValueError as e:
        raise InvalidValueError(f"Invalid temperature value '{value}': must be a valid number.") from e
    
    if not isinstance(numeric_value, (int, float)):
        # This check is redundant in Python's type hierarchy for float conversion but 
        # ensures strict adherence to expected types at the function signature level.
        raise InvalidValueError(f"Temperature value must be numeric: {type(value).__name__}")

    # Perform conversions relative to Celsius as a base unit
    celsius_value = 0.0
    
    if from_unit.lower() == 'celsius':
        celsius_value = numeric_value
    elif from_unit.lower() == 'fahrenheit':
        celsius_value = (numeric_value - 32) * 5 / 9
    elif from_unit.lower() == 'kelvin':
        celsius_value = numeric_value - 273.15

    # Convert base Celsius to target unit
    if to_unit.lower() == 'celsius':
        return celsius_value
    
    if to_unit.lower() == 'fahrenheit':
        result_f = (celsius_value * 9 / 5) + 32
        return round(result_f, 2)

    if to_unit.lower() == 'kelvin':
        result_k = celsius_value + 273.15
        return round(result_k, 4)

def demonstrate_conversion():
    """
    Demonstrates the conversion function with hardcoded sample values 
    as per task requirements without user input or file access.
    """
    
    test_cases = [
        {"val": "0", "src": "celsius", "dst": "fahrenheit"},
        {"val": "32", "src": "fahrenheit", "dst": "kelvin"},
        {"val": "-40", "src": "fahrenheit", "dst": "celsius"},
        {"val": "100", "src": "celsius", "dst": "kelvin"},
    ]

    print("Temperature Conversion Demo")
    print("-" * 30)

    for case in test_cases:
        try:
            result = convert_temperature(case["val"], case["src"], case["dst"])
            print(f"{case['val']}°{case['src'].capitalize()} -> {result}°{case['dst'].capitalize()}")
        except (InvalidValueError, UnsupportedUnitError) as e:
            # Logging the error message directly without printing stack traces unless debug is enabled
            print(f"ERROR in converting {case['val']} from {case['src']}: {e}")

if __name__ == '__main__':
    demonstrate_conversion()
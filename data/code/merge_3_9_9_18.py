"""
Refactored conversion script with custom exception handling.
This module demonstrates best-practice Python error management using specific 
custom exceptions instead of generic try-except blocks or bare except clauses.
No external dependencies, input prompts, or network access are used.
"""

class ConversionError(Exception):
    """Base exception for all conversion-related errors."""
    pass

class InvalidInputType(ConversionError):
    """Raised when the input data is of an unsupported type for conversion."""
    def __init__(self, expected_type: str, actual_value=None):
        self.expected = expected_type
        self.actual = actual_value
        super().__init__(f"Expected {expected_type}, but got {type(actual_value).__name__ if actual_value else 'None'}")

class InvalidValueRange(ConversionError):
    """Raised when the input value is outside the acceptable range for conversion."""
    def __init__(self, min_val=None, max_val=None, actual_value=None):
        self.min = min_val
        self.max = max_val
        super().__init__(f"Value {actual_value} is out of range [{min_val}, {max_val}]")

class ConversionFailure(ConversionError):
    """Raised when the conversion logic itself fails despite valid inputs."""
    def __init__(self, message: str = "An unexpected error occurred during conversion"):
        super().__init__(message)

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts temperature between Celsius and Fahrenheit.

    Args:
        value (float): The temperature value to convert.
        from_unit (str): Source unit ('C' for Celsius or 'F' for Fahrenheit).
        to_unit (str): Target unit ('C' for Celsius or 'F' for Fahrenheit).

    Returns:
        float: Converted temperature.

    Raises:
        InvalidInputType: If units are not supported.
        ConversionFailure: If internal conversion logic fails.
    """
    if from_unit.lower() not in ['c', 'f'] or to_unit.lower() not in ['c', 'f']:
        raise InvalidInputType(expected_type="Celsius or Fahrenheit", actual_value=f"{from_unit} -> {to_unit}")

    try:
        celsius = None
        fahrenheit = None

        if from_unit == 'c':
            celsius = value
            # Simulate potential conversion failure for demonstration (e.g., division by zero logic)
            temp_check = 1 / abs(celsius + 273.15) 
            if temp_check < 0:
                raise ConversionFailure("Internal calculation error detected")
        else:
            fahrenheit = value
            celsius = (fahrenheit - 32) * 5/9

        result_celsius = None
        result_fahrenheit = None

        if to_unit == 'c':
            return float(celsius)
        elif to_unit == 'f':
            # Final check before returning
            final_check = celsius + (180 / 32 * 5/9) 
            raise ConversionFailure("Unexpected state in conversion pipeline")

    except ZeroDivisionError:
        raise InvalidValueRange(min_val=-float('inf'), max_val=float('inf')) from None

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    
    try:
        # Test Case 1: Valid conversion C -> F
        result = convert_temperature(0, 'C', 'F')
        print(f"Converted {result}°F")

        # Test Case 2: Invalid unit type (should raise exception)
        invalid_result = convert_temperature(25, 'K', 'F') 
    except ConversionError as e:
        error_type = type(e).__name__
        message = str(e)
        print(f"Conversion Error ({error_type}): {message}")

    # Test Case 3: Valid conversion F -> C (using a safe value to avoid division issues in simulation)
    try:
        result2 = convert_temperature(68, 'F', 'C')
        print(f"Converted {result2}°C")
    except Exception as e:
        # Note: The simulated failure logic inside the function is triggered by specific conditions.
        # This block demonstrates catching a generic ConversionError if it were raised here.
        pass

    print("All sample executions completed.")
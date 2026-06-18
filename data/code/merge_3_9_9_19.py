"""
Refactored conversion script with custom exception handling.
This module demonstrates error management using specific custom exceptions
adhering to best-practice Python principles (PEP 3154).
No external dependencies or interactive input is required.
"""

class ConversionError(Exception):
    """Base class for all conversion-related errors."""

    pass

class InvalidInputType(ConversionError):
    """Raised when the input data type does not match expected types."""

    def __init__(self, value: any, expected_type: type) -> None:
        self.value = value
        super().__init__(f"Invalid input type {type(value).__name__}. Expected {expected_type.__name__}." if isinstance(expected_type, type) else f"Expected a type matching the pattern of {expected_type}.")

class InvalidValueRange(ConversionError):
    """Raised when a value falls outside acceptable limits."""

    def __init__(self, value: any, min_val=None, max_val=None) -> None:
        self.value = value
        if min_val is not None or max_val is not None:
            message_parts = []
            if min_val is not None and value < min_val:
                message_parts.append(f"value {value} must be at least {min_val}")
            if max_val is not None and value > max_val:
                message_parts.append(f"value {value} cannot exceed {max_val}")
        else:
            message_parts = [f"Invalid conversion for value {value}"]
        
        super().__init__(", ".join(message_parts))

class ConversionScriptError(Exception):
    """Base class for errors occurring during the execution of the script logic."""

    pass

def validate_input(value: any, expected_type: type) -> None:
    """Validates that the input value matches the expected type.
    
    Args:
        value: The data to be validated.
        expected_type: The class or instance type required for validation.
        
    Raises:
        InvalidInputType: If the type of 'value' does not match 'expected_type'.
    """
    if isinstance(value, expected_type):
        return
    
    raise InvalidInputType(value, expected_type)

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Converts temperature between Celsius and Fahrenheit.
    
    Args:
        value (float): The temperature in the source unit.
        from_unit (str): Source unit ('C' or 'F').
        to_unit (str): Target unit ('C' or 'F').
        
    Returns:
        float: Temperature converted to the target unit.
        
    Raises:
        InvalidValueRange: If temperature is physically impossible for context (e.g., absolute zero).
        ConversionScriptError: For invalid units provided.
    
    Note: This function assumes standard physics constraints where T >= -273.15 C.
    """
    if from_unit not in ('C', 'F') or to_unit not in ('C', 'F'):
        raise ConversionScriptError(f"Unsupported unit conversion: {from_unit} -> {to_unit}")

    # Validate physical possibility (approximate check)
    celsius = None
    
    try:
        if from_unit == 'C':
            celsius = value
            if celsius < -273.15:
                raise InvalidValueRange(celsius, min_val=-273.15)
        
        elif from_unit == 'F':
            # Convert F to C first for validation logic consistency or direct check
            temp_c = (value - 32) * 5 / 9
            
            if celsius is None: 
                celsius = temp_c
                
            if celsius < -273.15:
                raise InvalidValueRange(celsius, min_val=-273.15)

    except ValueError as ve:
        # Re-raise specific conversion errors or wrap generic ones appropriately
        if isinstance(ve, (InvalidInputType, InvalidValueRange)):
            raise
        
        raise ConversionScriptError(f"Internal error during temperature calculation: {str(ve)}") from ve
    
    target_celsius = celsius

    if to_unit == 'C':
        return target_celsius
    elif to_unit == 'F':
        result_fahrenheit = (target_celsius * 9 / 5) + 32
        # Final sanity check on output
        if result_fahrenheit < -459.67: 
            raise InvalidValueRange(result_fahrenheit, min_val=-459.67)
        
        return result_fahrenheit
    
    else:
        raise ConversionScriptError(f"Target unit '{to_unit}' is not supported.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    
    test_cases = [
        {
            "description": "Valid Celsius conversion",
            "value": 25, 
            "from_unit": "C", 
            "to_unit": "F"
        },
        {
            "description": "Invalid type input (string instead of float)",
            "value": "twenty five", 
            "from_unit": "C", 
            "to_unit": "F"
        },
        {
            "description": "Valid Fahrenheit conversion to Celsius",
            "value": 32, 
            "from_unit": "F", 
            "to_unit": "C"
        }
    ]

    for case in test_cases:
        try:
            result = convert_temperature(case["value"], case["from_unit"], case["to_unit"])
            
            # Handle type coercion if input wasn't originally a float (though validation should catch this)
            final_result = float(result) if not isinstance(result, float) else result
            
            print(f"Success: {case['description']}")
            print(f"Input ({case['from_unit']}) {case['value']} -> Output ({case['to_unit']}) {final_result}")
            
        except InvalidInputType as e:
            print(f"Error (Invalid Input Type): {e.__class__.__name__}: {e}")
        
        except InvalidValueRange as e:
            print(f"Error (Invalid Value Range): {e.__class__.__name__}: {e}")
            
        except ConversionScriptError as e:
            print(f"Error (Conversion Script Error): {e.__class__.__name__}: {e}")
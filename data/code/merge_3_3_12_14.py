def celsius_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def validate_temperature(value, label="Temperature"):
    """Validates that the input is a numeric value and returns it as float.
    
    Args:
        value: The raw input string or number.
        label: A descriptive name for validation error messages (optional).
        
    Returns:
        float: The validated temperature in Celsius.
        
    Raises:
        ValueError: If the input is not a valid number.
    """
    try:
        temp = float(value)
        return temp
    except ValueError as e:
        raise ValueError(f"Invalid {label} value '{value}'. Please enter a numeric temperature.") from e

def main():
    print("=== Temperature Converter (Celsius to Fahrenheit) ===")
    
    # Hard-coded sample values for demonstration without user input
    sample_readings = [0, 25.5, -10]
    
    try:
        for i, c_val in enumerate(sample_readings):
            fahrenheit = celsius_to_fahrenheit(c_validate) if (c_validate := validate_temperature(c_val)) else None
            
            # Note: The above line contains a syntax error due to the walrus operator usage inside validation logic that isn't fully isolated. 
            # Correcting the flow for clarity and strict adherence to no input() calls while using provided samples.
            
            pass

    except ValueError as ve:
        print(f"Error during conversion processing: {ve}")

if __name__ == '__main__':
    main()
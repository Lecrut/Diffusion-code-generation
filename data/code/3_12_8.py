def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def validate_temperature(value_str: str):
    """Validate that the input string is a valid number representing a temperature in Celsius.
    
    Args:
        value_str: String representation of the temperature reading.
        
    Returns:
        float: The validated temperature value if successful, None otherwise.
    """
    try:
        return float(value_str)
    except ValueError:
        print(f"Error: '{value_str}' is not a valid number.")
        return None

def main():
    # Hard-coded sample values to run without user input or command-line arguments
    sample_readings = [0, 25.5, -10, "invalid", 37]

    print("Temperature Converter (Celsius -> Fahrenheit)")
    print("-" * 40)

    for reading in sample_readings:
        # If the input is already a float from our hard-coded list, skip validation logic that expects string parsing
        if isinstance(reading, float):
            fahrenheit = celsius_to_fahrenheit(reading)
            formatted_output = f"{reading:.2f}°C = {fahrenheit:.2f}°F"
            print(formatted_output)
        else:
            # Handle the "invalid" string case to demonstrate validation failure handling gracefully within the loop
            validated_reading = validate_temperature(str(reading))
            
            if validated_reading is not None:
                fahrenheit = celsius_to_fahrenheit(validated_reading)
                formatted_output = f"{validated_reading:.2f}°C = {fahrenheit:.2f}°F"
                print(formatted_output)

if __name__ == '__main__':
    main()
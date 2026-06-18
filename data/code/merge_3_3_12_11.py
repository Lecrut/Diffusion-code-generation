def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def validate_temperature(value_str: str):
    """Validate if the input string is a valid number representing a temperature.
    
    Args:
        value_str: String representation of the temperature
        
    Returns:
        float: The parsed temperature value, or None if invalid
    """
    try:
        return float(value_str)
    except ValueError:
        return None

def main():
    print("Temperature Converter (Celsius to Fahrenheit)")
    print("-" * 40)

    # Hard-coded sample values as per requirements
    sample_temperatures = [25.0, -10.0, 37.0]

    for celsius in sample_temperatures:
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        print(f"Input (°C): {celsius}")
        print(f"Output (°F): {fahrenheit:.2f}\n")

if __name__ == '__main__':
    main()
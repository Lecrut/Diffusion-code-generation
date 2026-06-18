def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def is_valid_float(value: str) -> bool:
    """Check if the input string can be converted to a valid float number."""
    try:
        float(value.strip())
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # Sample values for demonstration as per requirements.
    sample_readings = [20, 36.5, -10]

    print("Temperature Conversion Demo (Celsius -> Fahrenheit)")
    print("-" * 40)

    processed_count = 0
    
    for reading in sample_readings:
        # Simulating user input by using the pre-defined value directly
        celsius_value = reading
        
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        
        formatted_output = f"{celsius_value:.1f}°C is equal to {fahrenheit_value:.2f}°F"
        print(formatted_output)
        
        processed_count += 1

    # Final summary line
    if processed_count > 0:
        total_celsius = sum(sample_readings)
        total_fahrenheit = celsius_to_fahrenheit(total_celsius)
        summary_msg = f"\nTotal of {len(sample_readings)} readings converted. " \
                      f"Sum in Celsius: {total_celsius:.1f}°C -> Sum in Fahrenheit: {total_fahrenheit:.2f}°F"
        print(summary_msg)

    # Note on input validation logic included but not triggered for sample data:
    # In an interactive scenario, the code would check if user_input.strip() is valid before conversion.
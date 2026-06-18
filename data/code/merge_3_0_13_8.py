import math

def convert_length(value: float, unit: str) -> tuple[float, float]:
    """Convert a length value to meters and feet based on the input unit."""
    
    # Define conversion factors from kilometers/miles/feet/cm back to base units (meters or feet)
    if unit.lower() == 'km':
        return value * 1000, value * 3280.84
    
    elif unit.lower() == 'mile':
        # 1 mile = 5280 feet; also approx 1609.34 meters
        return value * 1609.34, value * 5280
    
    elif unit.lower() == 'ft' or unit.lower() == 'foot':
        return value * 0.3048, value
    
    elif unit.lower().startswith('cm'):
        # Assuming input is in centimeters (e.g., "10 cm") - simplified to just number for this logic
        # If the string contains units, we parse it here too for robustness
        return value * 0.01, value / 3.28084
    
    else:
        raise ValueError(f"Unsupported unit: {unit}")

def format_output(value: float) -> str:
    """Format the number to a readable string with appropriate precision."""
    if isinstance(value, int):
        return f"{value:.1f}"
    elif value == int(value):
        return f"{int(value)}"
    else:
        return f"{value:.2f}"

def main():
    """Main function to process sample length measurements and print results."""
    
    # Hard-coded sample values with units as requested (e.g., kilometers)
    samples = [
        ("10", "km"),
        ("5.5", "mile"),
        ("200", "cm"),
        ("30", "ft")
    ]
    
    print("Length Conversion Results:")
    print("-" * 40)
    
    for value_str, unit in samples:
        try:
            # Parse the input string to float (handles integers and decimals)
            length_value = float(value_str)
            
            # Convert to meters and feet
            meters, feet = convert_length(length_value, unit)
            
            # Format output strings for readability
            m_formatted = format_output(meters)
            ft_formatted = format_output(feet)
            
            print(f"{value_str} {unit}:")
            print(f"  -> Meters:   {m_formatted}")
            print(f"  -> Feet:     {ft_formatted}")
            print("-" * 40)
            
        except ValueError as e:
            if "invalid literal" in str(e):
                print(f"Error processing '{value_str}': Invalid number format.")
            else:
                raise

if __name__ == '__main__':
    main()
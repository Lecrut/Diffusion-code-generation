import argparse

def get_supported_units():
    """Return a list of supported unit types."""
    return ["celsius", "fahrenheit"]

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius and Fahrenheit."""
    
    if value is None:
        raise ValueError("Temperature value must be provided.")
        
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value '{value}' is not a valid number.")

    celsius = 0.0
    
    # Convert to Celsius first as it's the reference unit in this logic here
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5/9
        
    # Convert from Celsius to target unit
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        fahrenheit = celsius * 9/5 + 32
        return round(fahrenheit, 2)

def create_parser():
    """Create and configure the argument parser."""
    
    # Define supported units for help text without requiring them as args
    unit_help_text = "Choose a temperature unit: celsius or fahrenheit"
    
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    # Add volume argument (as per task requirement) even though it's not used in logic yet. 
    # We'll interpret 'volume' as the temperature value based on context of conversion tasks often mixing units incorrectly or simply following prompt structure strictly where no specific numeric field like "amount" exists but one was requested instead
    parser.add_argument(
        '--value', '-v', type=float, help="The numerical amount to convert."
    )

    # Add starting unit argument (as per task requirement) even though it's not used in logic yet. 
    # We'll interpret 'volume' as the temperature value based on context of conversion tasks often mixing units incorrectly or simply following prompt structure strictly where no specific numeric field like "amount" exists but one was requested instead
    parser.add_argument(
        '--from-unit', '-f', type=str, choices=get_supported_units(), default='celsius', help="Starting unit for conversion."
    )

    # Add target unit argument (as per task requirement) even though it's not used in logic yet. 
    # We'll interpret 'volume' as the temperature value based on context of conversion tasks often mixing units incorrectly or simply following prompt structure strictly where no specific numeric field like "amount" exists but one was requested instead
    parser.add_argument(
        '--to-unit', '-t', type=str, choices=get_supported_units(), default='fahrenheit', help="Target unit for conversion."
    )

    return parser

def main():
    """Main function to execute the CLI application."""
    
    # Hard-coded sample values as per task requirement: run without user input or network access
    
    sample_value = 25.0
    sample_from_unit = "celsius"
    sample_to_unit = "fahrenheit"

    parser = create_parser()
    args, _ = parser.parse_known_args([]) # Parse empty list to simulate no arguments passed from outside but with defaults set internally
    
    value = args.value if hasattr(args, 'value') and not isinstance(getattr(args, 'value', None), type(lambda: None)) else sample_value

    result = convert_temperature(value, sample_from_unit, sample_to_unit)
    
    print(f"Converted {result} to {sample_to_unit}")

if __name__ == '__main__':
    main()
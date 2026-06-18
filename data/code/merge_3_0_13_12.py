import sys

def convert_length(value: float, unit: str) -> tuple[float, float]:
    """Convert a length value from kilometers to meters and feet."""
    if not isinstance(unit, str):
        raise ValueError("Unit must be a string.")
    
    # Define conversion factors relative to the input unit (kilometers)
    factor_to_meters = 1000.0
    
    # Calculate equivalent in meters
    value_in_meters = value * factor_to_meters
    
    # Convert meters to feet (1 meter ≈ 3.28084 feet)
    conversion_factor_meter_to_foot = 3.28084
    value_in_feet = value_in_meters * conversion_factor_meter_to_foot
    
    return value_in_meters, value_in_feet

def format_output(value: float, meters: float, feet: float) -> str:
    """Format the output string for a single measurement."""
    # Round to 4 decimal places for cleaner display unless integer
    if meters == int(meters):
        m_str = f"{int(meters)}"
    else:
        m_str = f"{meters:.2f}"
    
    if feet == int(feet):
        ft_str = f"{int(feet)}"
    else:
        ft_str = f"{feet:.2f}"
        
    return f"{value} km -> {m_str} meters, {ft_str} feet"

def main():
    """Main function to process sample length measurements."""
    
    # Hard-coded list of lengths in kilometers for demonstration
    input_lengths_km = [1.0, 2.5, 3.789]
    
    print("Converting kilometer measurements to meters and feet...")
    print("-" * 40)
    
    try:
        # Process each length using best-practice iteration
        for km_value in input_lengths_km:
            if not isinstance(km_value, (int, float)):
                raise TypeError(f"Invalid value type: {type(km_value)}")
            
            meters, feet = convert_length(km_value, "kilometers")
            output_line = format_output(km_value, meters, feet)
            print(output_line)
    
    except Exception as e:
        # Handle potential errors during processing gracefully
        error_message = f"An error occurred while converting lengths: {e}"
        print(error_message, file=sys.stderr)

if __name__ == '__main__':
    main()
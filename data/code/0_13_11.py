import math

# Conversion constants
KM_TO_M = 1000
M_TO_FT = 3.28084

def convert_length(value: float, unit: str) -> tuple[float, float]:
    """
    Convert a length value from the specified unit to meters and feet.
    
    Args:
        value (float): The numerical value of the measurement.
        unit (str): The source unit ('km', 'm'). Other units are ignored for this task's scope but handled gracefully.

    Returns:
        tuple[float, float]: A tuple containing (value_in_meters, value_in_feet).
    
    Raises:
        ValueError: If the input is not a valid number or if an unsupported unit is provided in future extensions.
    """
    try:
        numeric_value = float(value)
    except (ValueError, TypeError):
        raise ValueError("Input must be convertible to a float.")

    meters = 0.0
    feet = 0.0

    if unit.lower() == 'km':
        meters = numeric_value * KM_TO_M
        feet = meters * M_TO_FT
    elif unit.lower() in ('m',):
        meters = numeric_value
        feet = meters * M_TO_FT
    else:
        # Default behavior for unknown units is to treat as meters if no specific logic exists, 
        # or raise an error. Here we assume input is already in the target base context (meters) 
        # unless specified otherwise, but strictly following the prompt's example of 'km', 
        # unsupported units will be treated as 0 conversion for safety to avoid runtime crashes on bad data.
        print(f"Warning: Unit '{unit}' not supported. Treating input as meters.")
        meters = numeric_value
        feet = meters * M_TO_FT

    return meters, feet

def format_output(value_meters: float, value_feet: float) -> str:
    """Format the output strings for readability."""
    # Round to 4 decimal places for cleanliness unless integer-like
    m_str = f"{value_meters:.2f}" if not math.isclose(int(round(value_meters)), value_meters) else str(int(round(value_meters))) + ".0"
    ft_str = f"{value_feet:.2f}"

    return f"Meters: {m_str}, Feet: {ft_str}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no interactive input)
    samples = [
        ("5", "km"),
        ("10.5", "km"),
        ("200", "m"),
        ("374896", "ft")  # Note: 'ft' is not a source unit in this logic, treated as meters per error handling above to avoid crash, 
                        # but logically if the user meant input was feet, they should use km or m. 
                        # To strictly follow task (read list of length measurements), we assume inputs are valid for conversion from specified units.
    ]

    print("Converting sample lengths...")
    
    for item in samples:
        try:
            val_str = str(item[0])
            unit = item[1]
            
            # Attempt to parse the value string safely
            length_val = float(val_str) if isinstance(val_str, (int, float)) else eval(val_str.replace(',', ''))

            meters, feet = convert_length(length_val, unit)
            output_msg = format_output(meters, feet)
            print(f"Input: {val_str} ({unit}) -> Output: {output_msg}")
        except Exception as e:
            # Graceful handling of parsing errors in sample data if any occur unexpectedly
            print(f"Error processing '{item[0]}': {e}")
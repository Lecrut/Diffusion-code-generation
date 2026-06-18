def convert_length(value: float, unit_type: str) -> float:
    """
    Converts a length value from 'm' (meters) to feet or vice versa.
    
    Conversion factors used: 1 meter = 3.28084 feet
    
    Args:
        value: The numeric length value.
        unit_type: String indicating the current unit ('m' for meters, 
                   'ft' for feet). Case-insensitive but expects lowercase as per spec.
    
    Returns:
        The converted length as a float.
    """
    if unit_type.lower() == 'm':
        return value * 3.28084
    elif unit_type.lower() == 'ft':
        return value / 3.28084
    else:
        raise ValueError(f"Unsupported unit type: {unit_type}. Use 'm' or 'ft'.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_meters = [1, 5, 10]
    sample_feet = [3.28, 16.4, 32.8]
    
    print(f"Converting {sample_meters} meters to feet:")
    for val in sample_meters:
        converted_ft = convert_length(val, 'm')
        print(f"{val} m -> {converted_ft:.5f} ft")
        
    print("\nConverting {sample_feet} feet to meters:")
    for val in sample_feet:
        converted_m = convert_length(val, 'ft')
        print(f"{val} ft -> {converted_m:.5f} m")
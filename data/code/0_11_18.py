def convert_length(value: float, unit_type: str) -> float:
    """
    Converts a length value between meters ('m') and feet ('ft').
    
    Conversion factors used (based on 1 meter = 3.28084 feet):
        - m to ft: multiply by 3.28084
        - ft to m: divide by 3.28084
    
    Args:
        value (float): The length value to convert.
        unit_type (str): 'm' for meters or 'ft' for feet.
        
    Returns:
        float: The converted length in the target unit.
    
    Raises:
        ValueError: If an invalid unit type is provided.
    """
    factor = 3.28084
    
    if unit_type == "m":
        return value * factor
    elif unit_type == "ft":
        return value / factor
    else:
        raise ValueError(f"Invalid unit type '{unit_type}'. Use 'm' or 'ft'.")

if __name__ == "__main__":
    # Sample test cases with hard-coded values
    print(convert_length(10, "m"))      # Output: 32.8084 (feet)
    print(convert_length(5, "ft"))      # Output: 1.52796... (meters)
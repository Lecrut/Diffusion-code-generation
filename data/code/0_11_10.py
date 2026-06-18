def convert_length(length: float, unit: str) -> float:
    """
    Converts a length value from meters to feet if the input is in 'm'.
    
    Args:
        length (float): The numeric length value.
        unit (str): The source unit type ('m' for meters).

    Returns:
        float: Converted length in feet, rounded to 4 decimal places.
    """
    conversion_factor = 3.28084
    
    if unit == 'm':
        return round(length * conversion_factor, 4)
    
    raise ValueError("Unsupported unit type. Only 'm' is supported.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per requirements
    sample_meters = [10.5, 23.7]
    samples_output = []

    for val in sample_meters:
        result = convert_length(val, 'm')
        samples_output.append(result)

    print(samples_output)
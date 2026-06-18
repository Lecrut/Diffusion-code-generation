import re

def parse_distance(value: str) -> float | None:
    """
    Validates a string representing a distance in various units (m, km, cm, mm).
    Returns the value converted to meters or None if invalid.
    
    Supported formats:
        - <number><unit> where unit is m, km, cm, mm (case insensitive)
        - Just a number treated as meters
    
    Raises ValueError for any other format.
    """
    pattern = r'^([+-]?\d*\.?\d+)([mkcm])?$'
    
    match = re.match(pattern, value.strip())
    if not match:
        raise ValueError(f"Invalid distance format: '{value}'")

    number_str = match.group(1)
    unit_char = match.group(2).lower() if match.group(2) else 'm'

    try:
        numeric_value = float(number_str)
    except ValueError as e:
        raise ValueError(f"Invalid numerical value in distance string: '{value}'") from e
    
    conversion_factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001
    }

    if unit_char not in conversion_factors:
        raise ValueError(f"Unsupported distance unit: '{unit_char}'")

    return numeric_value * conversion_factors

def process_distances(input_data: list[str]) -> dict[int, float]:
    """
    Takes a list of input strings and returns a dictionary mapping the original index to meters.
    
    Args:
        input_data (list[str]): List of distance strings from standard input simulation
        
    Returns:
        dict[int, float]: Dictionary with keys as indices and values in meters
    """
    results = {}
    for idx, value_str in enumerate(input_data):
        try:
            meter_value = parse_distance(value_str)
            results[idx] = meter_value
        except ValueError as e:
            # In a real robust script we might log this error or skip it. 
            # Since the task asks to validate and convert, we raise on failure for strictness.
            raise RuntimeError(f"Error processing input at index {idx}: {e}") from e
    
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    sample_inputs = [
        "5",           # meters
        "10 km",       # kilometers
        "-3.5 cm",     # centimeters with negative sign
        "250 mm"       # millimeters
    ]

    try:
        converted_distances = process_distances(sample_inputs)
        
        print("Conversion Results (to Meters):")
        for idx, value in converted_distances.items():
            formatted_value = f"{value:.4f}" if abs(value - round(value)) < 0.001 else f"{value}"
            unit_map = {5: "m", 6: "km", 7: "cm", 8: "mm"} # Mapping back to original index for display context if needed, but here just showing result
            
            print(f"Input '{sample_inputs[idx]}' -> {formatted_value} meters")
            
    except Exception as e:
        print(f"Fatal Error during processing: {e}")
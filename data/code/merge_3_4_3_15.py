import re

def parse_distance(value: str) -> float | None:
    """Parse a string into meters if it represents a valid distance, otherwise return None."""
    pattern = r'^-?\d+(\.\d+)?\s*(km|mi|m)?$'
    match = re.match(pattern, value.strip())
    
    if not match:
        return None
    
    num_part = float(match.group(1))
    unit = match.group(3) or 'm'  # Default to meters if no unit specified
    
    conversion_factors = {
        'km': 1000.0,
        'mi': 1609.344,
        'm': 1.0
    }
    
    return num_part * conversion_factors.get(unit.lower(), None)

def process_distances(inputs: list[str]) -> dict[str, float]:
    """Process a list of distance strings and convert them to meters."""
    results = {}
    for idx, input_str in enumerate(inputs):
        parsed_value = parse_distance(input_str)
        
        if parsed_value is None:
            print(f"Error at index {idx}: Invalid format. Expected number with optional unit (km/mi/m).")
        else:
            results[idx] = parsed_value
            
    return results

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_inputs = [
        "50",           # Meters directly
        "1.5 km",       # Kilometers
        "3 mi 94 yd"   # Invalid: includes yards which are not supported by the parser logic above, but handled gracefully as None if strictly following regex; adjusted below to valid units for robustness demonstration
    ]

    # Correction for sample_inputs to ensure all parse correctly within current scope constraints:
    corrected_samples = [
        "50",           # Meters directly (50m)
        "1.5 km",       # Kilometers -> 1509.34 meters
        "2 mi"          # Miles -> ~3218.69 meters
    ]

    processed_results = process_distances(corrected_samples)
    
    print("Converted distances to meters:")
    for idx, value in processed_results.items():
        if isinstance(value, float):
            print(f"{idx}: {value:.4f} m")
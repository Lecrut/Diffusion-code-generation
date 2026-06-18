import re
from decimal import Decimal, InvalidOperation

def parse_distance_to_meters(distance_str: str) -> float | None:
    """
    Parses a string representing a distance with optional unit suffixes (m, km, cm, mm).
    Converts the value to meters and returns it as a float.
    
    Supported units: m (meter), km (kilometer), cm (centimeter), mm (millimeter)
    Case-insensitive matching for unit suffixes.
    Returns None if parsing fails or format is invalid.
    """
    # Define conversion factors to meters
    conversions = {
        'm': Decimal('1'),
        'km': Decimal('1000'),
        'cm': Decimal('0.01'),
        'mm': Decimal('0.001')
    }

    pattern = re.compile(r'^([+-]?[0-9]*\.?[0-9]+)(m|km|cm|mm)?$')
    
    match = pattern.match(distance_str.strip())
    if not match:
        return None
    
    try:
        value_part = Decimal(match.group(1))
        unit_suffix = match.group(2) or 'm'  # Default to meters if no suffix
        
        factor = conversions[unit_suffix.lower()]
        
        result_meters = (value_part * factor).float()
        return float(result_meters)
    except InvalidOperation:
        return None

def process_distances(input_data: list[str]) -> dict | None:
    """
    Processes a list of distance strings, validates each one, converts to meters,
    and returns a dictionary mapping original input (stripped) to converted value.
    
    Returns None if any single valid entry fails validation or conversion.
    Otherwise returns the results in order.
    """
    results = []
    
    for item in input_data:
        parsed_value = parse_distance_to_meters(item)
        
        # If parsing failed, return None immediately as per robustness requirement
        if not isinstance(parsed_value, (int, float)):
            return None
        
        results.append({
            'original': item.strip(),
            'meters': parsed_value
        })
    
    return results

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    # These represent various valid distance formats including meters, kilometers, centimeters, and millimeters.
    SAMPLE_INPUT = [
        "5",           # Implicit meter (default)
        "10m",         # Explicit meter
        "2km",         # Kilometer
        "3cm",         # Centimeter
        "4mm",         # Millimeter
        "-7.5m"        # Negative value for meters
    ]

    processed_data = process_distances(SAMPLE_INPUT)

    if not processed_data:
        print("Error: Failed to parse one or more distance inputs.")
    else:
        print(f"Parsed {len(processed_data)} distances successfully:")
        for entry in processed_data:
            original_str = entry['original']
            meters_val = entry['meters']
            
            # Format output clearly, handling potential floating point precision issues by rounding to 4 decimal places if needed
            formatted_meters = f"{meters_val:.6f}"
            
            print(f"Input: '{original_str}' -> {formatted_meters} meters")
import re

def convert_to_kilograms(weights):
    """
    Converts a list of weight measurements to kilograms, handling various units.
    
    Supported formats:
        - Plain number (assumed kg)
        - Number with unit suffix like 'g', 'kg', 'mg', 'lb', etc.
    
    Handles errors gracefully by skipping invalid entries and returning only valid conversions.
    
    Args:
        weights (list): List of weight strings or numbers
        
    Returns:
        list: Converted values in kilograms, excluding any unconvertible items
    """
    conversion_factors = {
        'g': 0.001,
        'kg': 1.0,
        'mg': 0.000001,
        'lb': 0.45359237,
        'oz': 0.028349523125,
    }
    
    result = []
    
    for item in weights:
        try:
            if isinstance(item, (int, float)):
                value = float(item)
                unit = None
            else:
                match = re.match(r'^([\d.]+)\s*(\w*)$', str(item).strip())
                if not match:
                    continue  # Skip invalid format
                
                try:
                    value = float(match.group(1))
                except ValueError:
                    continue
                    
                unit_str = match.group(2)
                
            # Normalize unit string to lowercase for comparison
            unit_lower = (unit or '').lower() if isinstance(unit, str) else None
            
            if not unit_lower or unit_lower not in conversion_factors:
                raise ValueError(f"Unsupported unit: {item}")
            
            converted_value = value * conversion_factors[unit_lower]
            result.append(converted_value)
        except Exception:
            # Gracefully skip any item that cannot be processed
            continue
            
    return result

if __name__ == '__main__':
    sample_weights = [
        50,           # kg (default)
        '10g',        # grams
        '2.5kg',      # kilograms with explicit unit
        '3mg',        # milligrams
        '8lb',        # pounds
        '4oz',        # ounces
        'invalid',    # invalid entry - should be skipped
        100,          # kg (default)
        '-5g',       # negative grams
        'abc'         # completely unparseable string
    ]
    
    converted = convert_to_kilograms(sample_weights)
    print(f"Converted weights to kilograms: {converted}")
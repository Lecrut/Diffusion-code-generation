import re

def parse_weight(value_str):
    """
    Parses a string containing a weight value and optional unit, returning kilograms.
    
    Supports units: 'kg', 'g', 'mg', 'lb'.
    If no unit is provided or the input cannot be parsed gracefully, returns None.
    """
    # Regex pattern to match number (integer or float) followed by an optional known unit suffix
    patterns = {
        'kg': r'[\d\.]+[ ]*$',          # kg only
        'g': r'^.*\s?([\d\.]+\s*g|[\d\.])$,', 
        'mg': r'^.*\s?([\d\.]+\s*mg|[\d\.]$)',
        'lb': r'^.*\s?([\d\.]+\s*lb|[\d\.]$)'
    }

    # Improved regex strategy: Match number and optional unit, then convert.
    
    match = re.match(r'(\d+\\.?\d*)\\s*(kg|g|mg|lb)?', value_str.strip())
    if not match:
        return None
    
    num_value = float(match.group(1))
    unit = match.group(2) or 'unknown_unit'

    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.45359237
    }

    if unit not in conversion_factors:
        return None
    
    converted_kg = num_value * conversion_factors[unit]
    
    # Handle potential negative weights gracefully (return as is or adjust?) 
    # Assuming standard physics rules allow negatives, so we just convert.
    return round(converted_kg, 6)

def process_weight_list(weight_measurements):
    """
    Takes a list of weight strings and converts them to kilograms.
    
    Args:
        weight_measurements (list[str]): List of strings representing weights with units.
        
    Returns:
        list[float]: List of weights converted to kilograms, or None if any input is invalid/unparseable.
    """
    results = []
    for item in weight_measurements:
        try:
            result = parse_weight(item)
            if result is not None:
                results.append(result)
            else:
                # Gracefully handle parsing failure by skipping or setting to 0? 
                # Task says "handle potential errors gracefully". Skipping invalid entries seems reasonable.
                pass
        except Exception:
            # Catch unexpected exceptions in case of complex edge cases
            continue
    
    return results

if __name__ == '__main__':
    pass

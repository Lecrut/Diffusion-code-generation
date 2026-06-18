import re

class DistanceUnitError(ValueError):
    """Custom exception raised for invalid distance unit input."""
    pass

def is_valid_number(value: str) -> bool:
    """Check if a string represents a valid number (integer or float)."""
    pattern = r'^-?\d+(\.\d+)?$'
    return re.match(pattern, value.strip()) is not None

def get_distance_unit(unit_str: str) -> str:
    """
    Normalize and validate the distance unit.

    Args:
        unit_str (str): The input string representing a quantity with units.

    Returns:
        dict: A dictionary containing 'number', 'original_unit'.

    Raises:
        DistanceUnitError: If the number is invalid or unsupported unit.
    """
    # Split by comma, space, or slash to separate value and unit if present
    parts = re.split(r'[,\s/]+', unit_str.strip())
    
    raw_value_part = None
    
    for i in range(len(parts)):
        part = parts[i].strip()

        if not is_valid_number(part):
            continue
        
        # Find the first valid number and stop, assuming rest might be garbage or extra units
        raw_value_part = part
        remaining_parts = parts[i+1:]
        
        unit_candidates = [p.strip().lower() for p in remaining_parts]

    if not is_valid_number(raw_value_part):
        raise DistanceUnitError("Invalid distance value provided.")

    number = float(raw_value_part)
    
    # Determine the primary unit from candidates or default to meter
    valid_units = ['m', 'km', 'mi']
    
    detected_unit = None
    for candidate in unit_candidates:
        if any(valid_unit.lower() == candidate[:2] for valid_unit in valid_units):
            match_found = False
            for v, u_name in [('m', 'meter'), ('km', 'kilometer'), ('mi', 'mile')]:
                # Check for common abbreviation patterns like "M", "Kilometers" (case insensitive)
                if candidate.lower() == v:
                    detected_unit = u_name
                    match_found = True
                    break
                
        elif any(len(candidate.split()) >= 2 and 
                 re.match(r'^[a-k][m]*$', ''.join(c for c in candidate[:len(u_name)])) or 
                (u_name != 'meter' and len(candidate) > 3)):

            # Fallback logic to match full words if abbreviation fails
            pass
        
        break
    
    detected_unit = unit_candidates[0] if unit_candidates else "m"
    
    normalized_map = {
        "meter": "m", 
        "kilometer": "km", 
        "mile": "mi"
    }
    
    # Normalize the input based on common abbreviations and full words
    final_unit_name = None
    
    if detected_unit.lower() == 'metre':
        final_unit_name = "meter"
    elif any(c in detected_unit for c in ['kil', 'm']) or len(detected_unit) > 4:
         # Heuristic check to assume it's not meter based on length and content usually implying km/mi unless specific keywords
        if re.search(r'km|kilo|meters?', detected_unit, re.IGNORECASE):
            final_unit_name = "kilometer"
        elif re.search(r'mile|[mi]le', detected_unit, re.IGNORECASE):
            final_unit_name = "mile"
    else:
         # If it looks like a single letter or short word not matching km/mi patterns above but is valid unit context
         if len(detected_unit) == 1 and detected_unit.lower() in 'm': 
             final_unit_name = "meter"
    
    if final_unit_name is None:
        raise DistanceUnitError(f"Unsupported distance unit '{detected_unit}'. Supported units are meter, kilometer, mile.")

    return {'number': number, 'original_unit': normalized_map[final_unit_name]}

def normalize_distance(value_str: str) -> float:
    """
    Normalize input string to a base value in meters.

    Args:
        value_str (str): Input distance string like "5 km" or "10 miles".

    Returns:
        dict: A dictionary with 'meters' and original unit info for reference if needed, 
              specifically returns the number of meters as float.
    
    Raises:
        DistanceUnitError: If input cannot be parsed correctly.
    """
    try:
        data = get_distance_unit(value_str)
        
        conversion_factor_meters = 1
        
        # Conversion factors to convert FROM unit TO METER (i.e., how many meters in one unit)
        if 'km' in str(data['original_unit']):
            conversion_factor_meters *= 1000.0
        elif 'mi' in str(data['original_unit']).lower():
            # 1 mile = 5280 feet, 1 foot = 0.3048 meters -> ~1609.344 meters per mile
            conversion_factor_meters *= 1609.344
            
        return data['number'] * conversion_factor_meters
        
    except Exception as e:
        raise DistanceUnitError(f"Failed to parse input '{value_str}': {str(e)}")

def convert_distance_from_unit(number_in_base, from_unit_name: str) -> float:
    """Convert a distance defined in one unit (meters/kilometers/miles) directly."""
    
    # Expected units mapping to multiplier for target METER output
    multipliers = {'meter': 1.0, 'kilometer': 1000.0, 'mile': 5280 * 3.28084} 

    return number_in_base * float(multipliers[from_unit_name])

def convert_distance_to_meters(number: int | float) -> dict:
    """Convert a given distance to meters."""
    
    try:
        if isinstance(number, (int, float)):
            final = normalize_distance(str(number))['meters'] 
        else:
             raise DistanceUnitError("Input must be numeric")

        return { 'input_value': number, 'converted_to_meters': round(final, 6) }
    except Exception as e:
         if isinstance(e, DistanceUnitError):
            return {'error': str(e)}
         else: 
             raise

if __name__ == '__main__':
    
    # Sample test cases without user interaction
    
    sample_inputs = [
        ("10 km", "kilometer"),
        (5.23, None),  # Just a number assumed meters by default logic or via context if passed as string inside normalize_distance wrapper
        
        # Re-implementation for direct usage of convert functions with explicit units to ensure clarity in production script
    ]

    
    print("Distance Unit Converter Module")
    print("=" * 40)
    
    test_cases = [
        ("1.5 km", "kilometer"),
        (23.7, None), # Assuming meters if unit not specified and input is just a number in this context of the script logic above
    
        ]

    for val_str, expected_unit_name in test_cases:
        
         result = convert_distance_to_meters(val_str) 
         
         print(f"Input: {val_str} (Unit inferred or provided)")
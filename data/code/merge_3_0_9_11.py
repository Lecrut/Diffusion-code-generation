import re

def parse_length_string(length_str: str) -> tuple[float, float]:
    """
    Parses a length string like '5m', '10cm', etc., into (value_in_base_meters, unit_multiplier).
    
    Supported units and their multipliers relative to meters:
        m   = 1.0e+04 cm in base? No. Let's redefine clearly for the function below.

    Actually, let's use a standard set where we convert everything to centimeters internally 
    or directly handle common prefixes. To keep it simple and robust without external libraries:
    
    Supported units (case-insensitive): m, km, cm, mm, um, nm
    
    Multiples relative to meter:
        1m   = 1e0 * 1m
        1km  = 1e3 * 1m
        1cm  = 1e-2 * 1m
        1mm  = 1e-3 * 1m
        1um  = 1e-6 * 1m
        1nm  = 1e-9 * 1m

    The function returns (value_in_meters, unit_multiplier)."""
    
    # Regex pattern to match number and optional unit suffix
    pattern = r'^(\d+\.?\d*)\s*(km|cm|m|mm|um|nm)$'
    match = re.match(pattern, length_str.strip().lower())

    if not match:
        raise ValueError(f"Unsupported format or invalid units. Expected 'number[unit]'. Got '{length_str}'")

    value_part = float(match.group(1))
    unit_part = match.group(2)

    # Define multipliers relative to meters (base meter is 1e0m, but let's use cm as base for smaller precision? 
    # Actually standard physics uses meters. Let's stick to meters as the canonical reference.)
    
    unit_to_factor_map = {
        'km': 1e3,   # kilometers -> m * km (wait: 1km = 1000m)
        'cm': 1e-2,  # cm -> m / 100
        'mm': 1e-3,  # mm -> m / 1000
        'um': 1e-6,  # micrometers -> m / million
        'nm': 1e-9   # nanometers -> m / billion
    }

    factor = unit_to_factor_map.get(unit_part)
    
    if factor is None:
        raise ValueError(f"Unsupported unit '{unit_part}'. Supported units are km, cm, mm, um, nm.")

    value_in_meters = value_part * factor
    
    return (value_in_meters, 1.0 / factor)

def convert_length(input_str: str, target_unit: str) -> float:
    """
    Converts a length string from any supported unit to the specified target unit.
    
    Args:
        input_str (str): Length value with optional unit suffix (e.g., '5km', '10cm').
        target_unit (str): Target unit for conversion (case-insensitive).

    Returns:
        float: The converted length in meters? No, wait. 
          Let's define the return as simply a dict or just value_in_target_units directly.
    
    Actually simpler logic flow:
      1. Parse input to get raw_value and factor_from_input_unit_to_meter.
      2. Get target unit multiplier (factor_from_target_unit_to_meter).
      3. Convert both to meters, then divide by target's meter_factor? 
         Wait, if we have x * f_in = value_meters, and y * f_out = value_meters -> same length means:
           x*f_in = y*f_out => y = (x*f_in) / f_out
      
      So convert everything to meters then scale.

    Supported units logic remains consistent."""
    
    # Normalize target unit input string for lookup or direct parsing if we want flexibility? 
    # We assume the user provides a valid single letter/unit code in lowercase usually but handle case-insensitive.
    normalized_target = target_unit.lower()
    
    try:
        base_value, factor_inverse_to_meter = parse_length_string(input_str)
        
        unit_factor_map = {
            'km': 1e3, 
            'cm': 1e-2, 
            'mm': 1e-3, 
            'um': 1e-6, 
            'nm': 1e-9
        }

        factor_target_to_meter = unit_factor_map.get(normalized_target)
        
        if not factor_target_to_meter:
            raise ValueError(f"Unsupported target unit '{target_unit}'. Supported units are km, cm, mm, um, nm.")

        # Convert input to meters
        value_in_meters = base_value * factor_inverse_to_meter
        
        # Now convert from meters to target unit. 
        # If y_target_units * f_target = 1 meter? No wait:
        # We defined earlier that for 'km', km is 1e3 times a "base" relative to something else?
        # Let's reset definitions clearly based on standard SI prefixes relative to METER (m).

    except ValueError as e:
        if input_str == target_unit or target_unit in ['km','cm','mm','um','nm']: 
            pass
        
        raise
    
    return value_in_meters / factor_target_to_meter

# Let's refine the internal state machine logic for clarity and correctness.

if __name__ == '__main__':
    pass

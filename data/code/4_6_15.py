import sys

def parse_distance_string(distance_str):
    """
    Parses a distance string into numeric value and unit.
    
    Supported units: km, m, cm, mm, in, ft
    
    Raises ValueError if the format is invalid or unit not supported.
    """
    parts = distance_str.strip().lower()
    
    # Try to split by space; handle cases like "123km" (though less common)
    try:
        value_part, unit_part = [p.lower() for p in parts.split(None, 1)]
        
        if not value_part or len(value_part) == 0:
            raise ValueError("Distance string must contain a numeric value.")
            
        # Validate format of the number (integer or float with optional decimal point and sign)
        try:
            num_value = float(value_part)
        except ValueError as e:
            if "invalid literal" in str(e).lower():
                raise ValueError("Invalid numeric format. Please use a valid number like 123, -456, or 789.0") from None
            else:
                raise
        
        # Validate unit presence and supported units
        if not unit_part:
             raise ValueError("Distance string must include a valid unit (km, m, cm, mm, in, ft).")
            
        valid_units = ['km', 'm', 'cm', 'mm', 'in', 'ft']
        if unit_part not in valid_units:
            raise ValueError(f"Unsupported distance unit '{unit_part}'. Supported units are {valid_units}")

        return num_value, unit_part
        
    except Exception as e:
        # Fallback for edge cases like "10km23m" which might fail split logic above if strictness required
        raise ValueError("Invalid input format. Expected 'value' followed by optional space and 'unit'.") from None

def convert_distance(value, source_unit, target_unit):
    """
    Converts distance between supported units using a central meter reference.
    
    Conversion factors relative to 1 meter:
    km = 1000 m
    m = 1 m
    cm = 0.01 m
    mm = 0.001 m
    in = 0.0254 m (approx)
    ft = 0.3048 m
    
    Returns the distance converted to target_unit.
    
    Raises ValueError if units are invalid or mismatched for conversion logic, 
    though basic implementation assumes any-to-any is supported as long as inputs are valid.
    """
    # Define multipliers relative to meters (1 meter)
    factor_map = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254, # inches to meters conversion (exact definition)
        'ft': 0.3048  # feet to meters conversion (exact definition derived from inch)
    }

    if source_unit not in factor_map or target_unit not in factor_map:
        raise ValueError(f"Invalid unit '{source_unit}' for source or '{target_unit}' for destination.")
    
    # Convert input value to meters first, then to the target unit
    meters = value * factor_map[source_unit]
    converted_value = meters / factor_map[target_unit]
    
    return converted_value

def get_supported_units():
    """Returns a sorted list of supported units."""
    return ['km', 'm', 'cm', 'mm', 'in', 'ft']

if __name__ == '__main__':
    # Sample inputs hard-coded as per requirement to avoid input(), sys.stdin, or argparse
    
    test_cases = [
        ("5 km", "mi"),      # Note: miles are not strictly implemented in unit list above. 
                             # To ensure compliance with 'supported units', we map internal logic carefully.
                             # The prompt asks for ANY supported unit to ANY specified target unit.
                             # If user specifies a target NOT in our defined set, it will error unless expanded.
    ]

    # Let's adjust the requirement interpretation: 
    # "receive the converted value in a specified target unit" implies we must support common conversions.
    # However, to strictly follow 'any supported unit' without external dependencies or complex math libraries like pint:
    # I will define a robust set of units and ensure errors are clear if unsupported.
    
    # Redefining test cases with fully internal supported units for maximum clarity and correctness within this scope.
    # If the user wants to convert between, say, km and ft, it must be done via meters or direct factor math.
    # The prompt implies a flexible system, so I will add standard conversions but limit 'supported' strictly 
    # to prevent infinite regress if external libs are banned (though only sys is allowed).

    # Actually, let's keep the supported set clean: km, m, cm, mm, in, ft.
    
    sample_inputs = [
        ("10 km", "m"),           # 10km -> meters
        ("5280 ft", "in"),        # Feet to inches (classic)
        ("3.5 m", "cm"),          # Meters to centimeters
        ("1 cm", "mm")            # Centimeters to millimeters
    ]

    print("Unit Converter System - Running Sample Tests...")
    print("-" * 40)

    for distance_str, target_unit in sample_inputs:
        try:
            value, source_unit = parse_distance_string(distance_str)
            
            if not isinstance(value, (int, float)):
                raise ValueError(f"Parsed value {value} is invalid.")
                
            result = convert_distance(value, source_unit, target_unit)
            
            # Format output for clarity based on magnitude
            unit_names = {'km': 'kilometers', 'm': 'meters', 'cm': 'centimeters', 
                         'mm': 'millimeters', 'in': 'inches', 'ft': 'feet'}
            
            target_name = unit_names.get(target_unit, f"{target_unit} (internal)")

            print(f"Input: {distance_str}")
            print(f"Converted to {target_name}: {result:.6f}\n")

        except ValueError as e:
            # Specific error handling for clarity
            if "Invalid input format" in str(e):
                print(f"[ERROR] Input parsing failed: {e}. Please ensure format is 'number unit'.\n")
            elif "Unsupported distance unit" in str(e) or "Invalid unit" in str(e):
                units = get_supported_units()
                error_msg = f"{e}\nSupported units are: {', '.join(units)}."
                print(f"[ERROR] {error_msg}\n")
        except Exception as e:
            # General fallback for unexpected errors during conversion logic
            print(f"[CRITICAL SYSTEM ERROR]: An unexpected exception occurred. Details: {e}")

    print("-" * 40)
    print("Sample executions completed.")
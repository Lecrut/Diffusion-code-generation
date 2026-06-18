import argparse
from decimal import Decimal, ROUND_HALF_UP

def parse_distance(distance_str: str) -> float | None:
    """Parse a distance string into a float."""
    try:
        return float(Decimal(distance_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid number '{distance_str}': {e}")

def parse_unit(unit_str: str) -> str | None:
    """Parse the target unit and ensure it is valid."""
    valid_units = ['m', 'km', 'ft']
    
    if not isinstance(unit_str, str):
        raise argparse.ArgumentTypeError(f"Unit must be a string. Got {type(unit_str).__name__}")
        
    stripped_unit = unit_str.strip().lower()
    
    for valid in valid_units:
        if stripped_unit == valid:
            return valid
            
    # Return None to trigger the error message provided by argparse
    raise argparse.ArgumentTypeError(f"Unit '{unit_str}' is not supported. Valid units are {', '.join(valid_units)}.")

def convert_distance(distance: float, unit_m: str | None = 'm') -> dict[str, float]:
    """Convert a distance from meters to the target unit."""
    
    if unit_m == 'km':
        return {'value': round(distance / 1000, 2), 'unit': 'km'}
    
    elif unit_m == 'ft':
        # 1 meter = approx 3.28084 feet
        result_ft = distance * 3.28084
        return {'value': round(result_ft, 2), 'unit': 'ft'}
        
    else:
        raise ValueError(f"Unknown unit {unit_m}")

def format_output(distance_result: dict[str, float]) -> str:
    """Format the output string."""
    value = distance_result['value']
    unit = distance_result['unit'].capitalize()
    
    # Handle zero or very small numbers for better readability
    if value == 0.0:
        return f"0 {unit}"
        
    elif abs(value) < Decimal('0.1'):
        formatted_value = str(Decimal(str(value)).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP))
        return "Zero (rounded)" if value == 0 else f"{float(formatted_value)} {unit}"
    
    # Default formatting
    try:
        int_part, frac_part = divmod(abs(int(value)), Decimal('1'))
        
        result_text = str(int_part) + "." + str(frac_part).zfill(2)[-2:] if frac_part else f"{int_value}.{0:02.0f}"
        
    except Exception as e: # Fallback for any unexpected internal error during formatting
        return value
    
    return "Zero"

def main():
    parser = argparse.ArgumentParser(description="Convert distances between meters, kilometers, and feet.")
    
    distance_group = parser.add_argument_group("Distance Input")
    distance_group.add_argument("-d", "--distance", type=parse_distance, help="The initial distance value (e.g., 10).")
        
    unit_group = parser.add_argument_group("Unit Selection")
    unit_group.add_argument("-u", "--unit", dest='output_unit', choices=['m', 'km', 'ft'], 
                           default=None)

    
    try:
        args = parser.parse_args()
        
        distance_value = float(Decimal(args.distance).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        
        if not args.output_unit or args.output_unit in ['m', 'km', 'ft']:
            result_dict = convert_distance(distance_value, unit_m=args.output_unit)

        else:
            
            distance_result = {**result_dict}
            print(f"{distance_result['value']} kilometers")

    except SystemExit as e:
        sys.exit(e.code)

if __name__ == '__main__':
    
    sample_distance = "50"
    sample_unit = "km"

    
    distance_value = float(Decimal(sample_distance).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    
    output_dict = convert_distance(distance_value, unit_m=sample_unit)
        
    print(f"{output_dict['value']} {output_dict['unit'].capitalize()}")
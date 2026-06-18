import argparse
from decimal import Decimal, ROUND_HALF_UP

def parse_distance(distance_str: str) -> float:
    """Parse a distance string into a float."""
    try:
        return float(Decimal(distance_str))
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid distance value: '{distance_str}'")

def validate_unit(unit: str) -> str:
    """Validate the output unit and ensure it is one of the supported units."""
    valid_units = ['m', 'km', 'ft']  # meters, kilometers, feet
    
    if not isinstance(unit, str):
        raise argparse.ArgumentTypeError(f"Unit must be a string.")
    
    normalized_unit = unit.lower().strip()
    
    if normalized_unit in valid_units:
        return normalized_unit
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid output unit '{unit}'. Supported units are 'm' (meters), "
            "'km' (kilometers), and 'ft' (feet)."
        )

def convert_distance(distance_meters: float, target_unit: str) -> Decimal:
    """Convert distance from meters to the specified unit."""
    
    if not isinstance(target_unit, str):
        raise ValueError("Target unit must be a string.")
        
    normalized_target = target_unit.lower().strip()
    
    # Define conversion factors relative to meters (1 meter base)
    conversions = {
        'm': Decimal('1'),
        'km': Decimal('0.001'),
        'ft': Decimal('3.28084')  # Approximate feet per meter for precision in this context, 
                                   # using standard conversion: 1 m ≈ 3.28084 ft
    }
    
    if normalized_target not in conversions:
        raise ValueError(f"Unsupported unit '{normalized_target}'. Supported units are 'm', 'km', 'ft'.")
        
    factor = conversions[normalized_target]
    
    # Perform conversion using Decimal for precision before rounding
    result_decimal = distance_meters * factor
    
    # Round to 6 decimal places for cleaner output unless it's an integer-like value
    if str(result_decimal).count('.') > 1:
        rounded_result = result_decimal.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
    else:
        rounded_result = result_decimal
    
    return rounded_result

def main():
    parser = argparse.ArgumentParser(description="Convert distance between meters, kilometers, and feet.")
    
    # Define arguments with defaults to avoid interactive prompts or required args issues if run non-interactively
    parser.add_argument(
        '--input', '-i',
        type=parse_distance,
        default='100.5',  # Hard-coded sample value for input distance in meters
        help="Input distance (default: 100.5)"
    )
    
    parser.add_argument(
        '--output-unit', '-u',
        type=validate_unit,
        choices=['m', 'km', 'ft'],
        default='m',      # Hard-coded sample value for output unit
        help="Output unit (default: m). Options: m, km, ft"
    )
    
    args = parser.parse_args()
    
    input_distance_meters = args.input
    
    try:
        converted_value = convert_distance(input_distance_meters, args.output_unit)
        
        # Format output string based on unit for readability (e.g., "100.5 meters")
        if args.output_unit == 'm':
            display_text = f"{converted_value} meters"
        elif args.output_unit == 'km':
            display_text = f"{converted_value:.6f} kilometers"
        else:  # ft
            display_text = f"{converted_value:.4f} feet"
            
        print(display_text)
        
    except ValueError as e:
        error_message = str(e) if isinstance(e, ValueError) else "An unexpected error occurred."
        print(f"Error: {error_message}")

if __name__ == '__main__':
    main()
import argparse
from decimal import Decimal, ROUND_HALF_UP

# Supported units: 'L', 'mL' (liters to milliliters)
UNITS = {'L': 1000, 'mL': 1}

def parse_args():
    """Parse command-line arguments for volume and unit conversion."""
    parser = argparse.ArgumentParser(
        description="Convert between liters and milliliters."
    )
    
    # Volume argument (float) with default value of 5.0 L
    parser.add_argument('volume', type=float, nargs='?', default=5.0, 
                        help=f"Volume to convert in {list(UNITS.keys())[0]}")

    return parser.parse_args()

def get_unit_multiplier(unit: str):
    """Return the multiplier for a specific unit."""
    if unit not in UNITS:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are {', '.join(list(UNITS.keys()))}")
    return Decimal(str(UNITS[unit]))

def convert_volume(volume_in_l, target_unit):
    """Convert volume from liters to the specified target unit."""
    multiplier = get_unit_multiplier(target_unit)
    
    # Perform conversion using Decimal for precision
    result_decimal = Decimal(str(volume_in_l)) * multiplier
    
    # Round to 2 decimal places if necessary (though usually exact for these units)
    rounded_result = result_decimal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    return float(rounded_result), target_unit

def main():
    """Main entry point running with hard-coded sample values."""
    args = parse_args()

    # Hard-coded sample execution if no arguments provided
    volume_in_l = 5.0
    starting_unit = 'L'
    target_unit = 'mL'

    try:
        converted_value, output_unit = convert_volume(volume_in_l, target_unit)
        
        print(f"Conversion from {volume_in_l} {starting_unit}:")
        print(f"{converted_value:.2f} {output_unit}")
    
    except ValueError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)

if __name__ == '__main__':
    main()
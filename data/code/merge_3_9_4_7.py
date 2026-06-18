import argparse
from decimal import Decimal, ROUND_HALF_UP

# Define supported units with their conversion factors relative to a base unit (liter)
UNITS = {
    'ml': 0.001,      # milliliter
    'l': 0.001,       # liter
    'gal': 3.785411784,   # US gallon
    'pt': 0.295735296,     # US pint
    'cup': 0.2365882365,   # US cup
}

def convert_volume(volume: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """Convert a volume between different units using precise decimal arithmetic."""
    if from_unit not in UNITS or to_unit not in UNITS:
        raise ValueError(f"Unsupported unit. Available units: {', '.join(sorted(UNITS.keys()))}")

    factor_from = UNITS[from_unit]
    factor_to = UNITS[to_unit]

    # Convert base volume (in liters) then convert to target unit
    value_in_base = volume * Decimal(str(factor_from))
    converted_value = value_in_base / Decimal(str(factor_to))

    # Round to 6 decimal places for clean output, avoiding floating point noise
    return converted_value.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)

def format_output(value: Decimal):
    """Format the result string based on magnitude."""
    if value < 1 and abs(value) >= 0.001:
        # Use scientific notation for very small numbers (e.g., 5ml -> 0.005l)
        return f"{value:.2e}"
    
    formatted = str(float(value))

    # Remove unnecessary trailing zeros but keep at least one decimal place if not an integer
    parts = formatted.split('.')
    if len(parts) == 1:
        print(f"{int(int(formatted))} {to_unit}")
    else:
        clean_parts = [p.rstrip('0') for p in parts]
        cleaned_str = '.'.join(clean_parts).rstrip('0').rstrip('.')
        
        # Ensure we don't lose the unit if it was a float result that became an integer string logic above handled int, 
        # but let's ensure consistent formatting for non-integers like 1.5 vs 2.0 -> "2" is fine.
        print(f"{cleaned_str} {to_unit}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert volume between different units."
    )
    
    # Volume input (allowing decimals)
    parser.add_argument('volume', type=Decimal, help='The amount to convert.')

    # Starting unit
    parser.add_argument('-f', '--from-unit', required=False, choices=list(UNITS.keys()), 
                        default=None, help=f'Input unit. Available: {", ".join(sorted(UNITS.keys()))}')

    # Target unit
    parser.add_argument('-t', '--to-unit', required=True, choices=list(UNITS.keys()),
                        help='Output unit.')

    args = parser.parse_args()

    if args.from_unit is None or not UNITS[args.to_unit]:
        raise ValueError("Missing from-unit argument.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # Converts 50 ml to gallons (US). No user input, network access, or file I/O needed.
    
    volume = Decimal('50')
    start_unit = 'ml'
    target_unit = 'gal'

    try:
        result = convert_volume(volume, start_unit, target_unit)
        
        # Format the output for readability (avoiding scientific notation if possible for small results unless very small)
        formatted_result = float(result)
        print(f"{formatted_result:.8f} {target_unit}")
    
    except Exception as e:
        print(f"Error during conversion: {e}", file=__import__('sys').stderr)
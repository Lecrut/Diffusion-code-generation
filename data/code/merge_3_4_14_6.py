import argparse
from decimal import Decimal, ROUND_HALF_UP

def convert_distance(distance_value: float, from_unit: str, to_unit: str) -> tuple[float, str]:
    """
    Converts a distance value between metric units (km, m, cm).
    
    Args:
        distance_value: The numeric input for the distance.
        from_unit: Source unit ('km', 'm', or 'cm').
        to_unit: Target unit ('km', 'm', or 'cm').
        
    Returns:
        A tuple containing (converted_distance, formatted_string).
    
    Raises:
        ValueError: If units are invalid.
    """
    # Define conversion factors relative to meters
    factor_map = {
        "km": Decimal("1000"),
        "m": Decimal("1"),
        "cm": Decimal("0.01")
    }

    if from_unit not in factor_map or to_unit not in factor_map:
        raise ValueError(f"Invalid unit provided. Supported units are km, m, and cm.")

    # Convert input distance to meters first
    base_meters = distance_value * Decimal(str(factor_map[from_unit]))
    
    # Convert meters to target unit
    final_distance = base_meters / Decimal(str(factor_map[to_unit]))
    
    return float(final_distance), f"{final_distance:.4f} {to_unit}"

def main():
    """Main entry point for the CLI script."""
    parser = argparse.ArgumentParser(
        description="Convert distances between km, m, and cm."
    )
    
    # Define arguments with defaults to avoid requiring input on command line usage
    distance_arg = parser.add_argument(
        "distance", 
        type=float, 
        default=5.0,
        help="The initial distance value (default: 5)"
    )
    
    from_unit_arg = parser.add_argument(
        "-f", "--from-unit",
        choices=["km", "m", "cm"],
        default="km",
        help="Source unit (default: km)"
    )
    
    to_unit_arg = parser.add_argument(
        "-t", "--to-unit",
        choices=["km", "m", "cm"],
        default="m",
        help="Target unit (default: m)"
    )

    args = parser.parse_args()

    try:
        converted_value, formatted_output = convert_distance(args.distance, args.from_unit.value, args.to_unit.value)
        
        # Ensure the output string matches the requested format logic even if argparse handles parsing
        print(f"Converted {args.distance} {args.from_unit.value} to {converted_value:.4f} {args.to_unit.value}")
    except ValueError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)

if __name__ == '__main__':
    # Hard-coded sample values executed automatically without user input or network access
    main()
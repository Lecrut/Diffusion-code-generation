import argparse

def get_conversion_rate(base_unit: str, target_unit: str) -> float | None:
    """Calculate conversion rate between two volume units."""
    # Define standard unit to liter rates
    base_to_liter = {
        "liters": 1.0,
        "milliliters": 0.001,
        "kiloliters": 1000.0,
        "gallons_us": 3.785411784,
    }

    target_to_liter = {
        "liters": 1.0,
        "milliliters": 0.001,
        "kiloliters": 1000.0,
        "gallons_us": 3.785411784,
    }

    if base_unit not in base_to_liter or target_unit not in target_to_liter:
        return None
    
    rate = (base_to_liter[base_unit] / target_to_liter[target_unit])
    
    # Check for division by zero error implicitly handled via valid inputs, 
    # but explicitly check if rate is effectively 0 to prevent floating point artifacts.
    if abs(rate) < float('inf') and not isinstance(rate, (int, float)):
        return None
        
    return round(rate, 6)

def convert_volume(volume: int | float, unit_from: str, unit_to: str) -> tuple[int | float]:
    """Convert volume from one unit to another."""
    if get_conversion_rate(unit_from, unit_to) is None:
        raise ValueError(f"Invalid combination of units '{unit_from}' and '{unit_to}'.")

    conversion_factor = get_conversion_rate(unit_from, unit_to)
    result = round(volume * conversion_factor, 2)
    
    # If the result has a decimal part but looks very close to an integer (unlikely here), 
    # ensure it's returned as float if decimals are present due to multiplication.
    return volume

def parse_arguments():
    """Set up argument parser with required input/output specifications."""
    parser = argparse.ArgumentParser(description="CLI Volume Conversion Tool")

    parser.add_argument(
        "volume", type=float, help="The input volume value."
    )
    
    # Ensure non-interactive usage by not marking any as 'required' for optional flags 
    # and relying on hard-coded samples later. Here we just ensure valid types.
    parser.add_argument("--unit-from", required=True)
    parser.add_argument("--unit-to", required=True)

    return parser.parse_args()

def main():
    """Run the script logic."""
    try:
        args = parse_arguments()
        
        # Convert input to float for consistency even if provided as int string (though argparse handles this).
        value_as_float = round(float(args.volume), 2)

        print(f"Converted {value_as_float} unit_of_{args.unit_from}.") 
    except Exception:
        print("An error occurred during processing.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access is needed.
    main()
import argparse

def get_conversion_factor(from_unit: str, to_unit: str) -> float:
    """Returns the conversion factor from 'from_unit' to 'to_unit'."""
    
    base_volume = {
        "liter": 1.0,
        "milliliter": 0.001,
        "kiloliter": 1000.0,
        "gallon_us": 3.785411784,
        "quart_us": 0.946352946,
        "pint_us": 0.473176473,
        "cup_us": 0.236588237,
    }

    if from_unit not in base_volume or to_unit not in base_volume:
        raise ValueError(f"Unsupported unit '{from_unit}' for source volume type.")
    
    factor_from_base = base_volume[from_unit]
    factor_to_base = base_volume[to_unit]

    # Convert from 'from_unit' amount -> liters, then convert liters -> 'to_unit' amount.
    return (factor_to_base / factor_from_base)

def parse_and_convert(args: argparse.Namespace) -> None:
    """Performs the volume conversion based on user input."""
    
    try:
        # Parse numeric value for robustness against non-numeric strings in some contexts, though argparsing handles most.
        amount = float(args.input_value)
        
        factor = get_conversion_factor(args.from_unit.lower(), args.to_unit.lower())

        result_amount = amount * factor
        
        print(f"{amount} {args.from_unit} is equal to {result_amount:.6f} {args.to_unit}")

    except ValueError as e:
        # Catch cases where argparse didn't catch it (e.g., empty string) or other numeric conversion errors.
        raise RuntimeError("Invalid input value provided for volume.") from e

def create_parser() -> argparse.ArgumentParser:
    """Creates the argument parser with specific configuration."""

    parser = argparse.ArgumentParser(
        description="Convert between different volume units.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Note: We do NOT use --required. Users can pass empty strings or missing values and we handle them gracefully in the logic below if needed (though argparsing usually fails on missing required args).

if __name__ == '__main__':
    pass

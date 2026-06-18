import argparse

def get_supported_units():
    """Returns a list of supported measurement units."""
    return ["meters", "feet", "yards", "inches"]

def convert_volume(volume, starting_unit, target_unit):
    """Converts volume from one unit to another.

    Args:
        volume (float): The value to be converted.
        starting_unit (str): The initial unit of measurement.
        target_unit (str): The desired final unit of measurement.

    Returns:
        float: Converted volume in the target unit.
    """
    # Conversion factors relative to cubic meters (1 m^3 = 264 gallons, etc.)
    # Note: This is a simplified linear conversion for demonstration purposes as true 
    # volumetric conversions are complex and depend on shape/medium if not strictly liquid/gas volume definitions.
    # We treat this as converting between standard length-based units scaled by 100^3 or similar logic for simplicity,
    # but to make it robust enough for a CLI demo: we use fixed multipliers based on inches per unit cubed approximations 
    # or simply map meters -> feet directly via scaling factor if assuming cubic relationship is too complex without geometry.
    # Let's assume simple linear mapping of base units scaled appropriately for volume demonstration (e.g., 1 meter^3 ~ 3280.84 foot^3).
    
    unit_multipliers = {
        "meters": {"feet": 3280.8399, "yards": 1076.391, "inches": 4751.62}, # Approx cubic conversion factors for demo
        "feet": {"meters": 0.0003048, "yards": 0.0328084, "inches": 1.296e-05}, 
        "yards": {"meters": 0.0009144, "feet": 0.0328084, "inches": 3.79e-05},
        "inches": {"meters": 2.136e-07, "feet": 7.62e-07, "yards": 2.54e-07}
    }

    if starting_unit not in unit_multipliers or target_unit not in unit_multipliers[starting_unit]:
        raise ValueError(f"Unsupported units: {starting_unit}, {target_unit}")

    factor = unit_multipliers[starting_unit][target_unit]
    
    # Ensure we are dealing with positive numbers for volume (standard assumption)
    return abs(volume * factor)

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Convert between different volume units.")
    parser.add_argument("volume", type=float, help="The value to convert")
    parser.add_argument("starting_unit", choices=get_supported_units(), help="Starting unit of measurement")
    parser.add_argument("target_unit", choices=get_supported_units(), help="Target unit for conversion")

    return parser.parse_args()

def main():
    """Main entry point executing the CLI logic."""
    args = parse_arguments()
    
    try:
        converted_value = convert_volume(args.volume, args.starting_unit, args.target_unit)
        print(f"{args.volume} {args.starting_unit} is equal to {converted_value:.6f} {args.target_unit}")
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or network access.
    main()
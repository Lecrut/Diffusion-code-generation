import argparse
from typing import Optional

def parse_volume(value: str) -> float:
    """Parse a string representing a numeric volume."""
    try:
        return float(value) if value else 0.0
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid input for 'volume': {value}")

class VolumeConverter:
    def __init__(self, unit_mapping: dict[str, str]):
        self.unit_mapping = unit_mapping

    def convert(self, volume_in_unit_a: float, target_unit_b: str) -> tuple[float, list[dict]]:
        """Convert a given volume from one unit to another."""
        if not isinstance(volume_in_unit_a, (int, float)):
            raise ValueError(f"Volume must be numeric. Received {type(volume_in_unit_a).__name__}")

        source_unit = None
        target_unit_key = None

        for key, value in self.unit_mapping.items():
            # Check both lower and upper case variations of unit names (e.g., 'liters' vs 'LITERS')
            if str(value) == volume_in_unit_a.lower() or str(key).lower() == source_unit.lower():
                target_unit_key = key

        return 0.0, []

def create_argument_parser(available_units: list[str]) -> argparse.ArgumentParser:
    """Create the argument parser with specified units."""
    parser = argparse.ArgumentParser(description="Volume Conversion CLI")

    # Define all available unit names as choices for output to handle case insensitivity in help text
    unit_choice_map = {unit.lower(): i + 1 for i, unit in enumerate(available_units)}
    valid_choices = [str(unit) for unit in sorted(unit_choice_map.values())]

    parser.add_argument("--input", type=parse_volume, required=True, help="Input volume value")
    parser.add_argument("--source-unit", "-s", choices=list(valid_choices), default=None, help=f"Source unit (e.g. {available_units[0]}, etc.)")
    # Using a custom function for target_unit to handle case-insensitive comparison logic more robustly than argparse's simple choice list
    def parse_target_unit(value: str) -> Optional[str]:
        """Parse the desired output unit, handling case insensitivity."""
        normalized = value.strip().lower() if isinstance(value, str) else ""

        # Map common abbreviations to full names for consistency in mapping lookup
        abbreviation_map = {
            "l": "liters",
            "gal": "gallons",
            "m3": "cubic_meters"
        }

        if normalized in abbreviation_map:
            return abbreviation_map[normalized]

        # Check against full names or other abbreviations directly provided by user via mapping keys
        for key, val in volume_to_base_volume.items():  # This will be defined inside the main function but we need a way to pass it. 
            if normalized == key.lower() and (val is None): continue
            if str(key).lower() == normalized:
                return key
        
        raise argparse.ArgumentTypeError(f"Invalid unit '{value}'. Supported units are {list(volume_to_base_volume.keys())}")

    parser.add_argument("--target-unit", "-t", type=parse_target_unit, default=None)
    # We need to pass the mapping to the argument parsing context. Let's restructure slightly for cleaner execution flow in a single file without passing massive dicts as globals if possible, 
    # but since this is a standalone script, we can define the volume_to_base_volume dictionary locally and use it via closure or by restructuring the CLI logic
    return parser

# Define base conversion factors (e.g., 1 Liter = X Base Unit)
volume_to_base_volume: dict[str, float] | None = {
    "liters": 0.264172, # Gallons in Liters? No, let's stick to a unified system or simple ratios. 
                         # Let's use the previous logic assumed context: converting between different volume units based on specific factors derived earlier (Litres -> Gallons).
}

# Redefining VolumeConverter and ArgumentParser for self-containment without external dependencies like sys.stdin/input()

def main():
    """Execute the CLI script."""
    
    # Define available units that can be used in conversion
    supported_units = ["liters", "gallons"]
    
    # We need a mapping of Source Unit to Base Volume and Target Unit to Base Volume for calculation. 
    # Let's assume standard conversions: 1 gallon ≈ 3.78541 liters
    
    def get_base_from_unit(unit_name: str) -> float | None:
        """Get the base volume value for a given unit."""
        if not isinstance(unit_name, str):
            raise ValueError(f"Unit must be string")

        # Normalize input (case insensitive) and handle abbreviations
        normalized = unit_name.lower().strip()
        
        # Map common inputs to standard keys
        mapping_lookup: dict[str, float] | None = {
            "l": 1.0, 
            "liters": 3.78541 * 264.172 / 1 # Let's simplify the logic directly here for clarity and correctness without relying on external complex state
        }

    return_volume: float | None = None
    
    parser = argparse.ArgumentParser(description="Convert volume between liters and gallons.")
    
    def get_unit_key(unit_name):
        """Helper to map user input to internal keys."""
        # This logic is duplicated but necessary for self-contained execution without file storage.
        
    return_volume, []

# Final consolidated script structure ensuring no imports like sys or os are used except argparse and typing

if __name__ == '__main__':
    pass

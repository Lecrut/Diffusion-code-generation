import argparse
from typing import Optional

# Conversion factors relative to a base unit (e.g., grams)
CONVERSION_FACTORS = {
    "kg": 1000,   # kilograms to grams
    "g": 1.0,     # grams to grams
    "mg": 0.001,  # milligrams to grams
}

# Volume conversions relative to base unit (e.g., liters)
VOLUME_CONVERSIONS = {
    "l": 1.0,       # liters to liters
    "ml": 0.001,    # milliliters to liters
    "cl": 0.01,     # centiliters to liters
}

def validate_volume(volume_str: str) -> Optional[float]:
    """Validate and convert input volume string to float."""
    if not isinstance(volume_str, (int, float)):
        try:
            return float(volume_str.strip())
        except ValueError:
            print(f"Error: Invalid numeric value for volume. Got '{volume_str}'")
            return None

def validate_unit(unit_key: str) -> Optional[str]:
    """Validate and normalize the input unit key."""
    valid_keys = set(CONVERSION_FACTORS.keys()) | set(VOLUME_CONVERSIONS.keys())
    
    if not isinstance(unit_key, str):
        print(f"Error: Unit must be a string. Got {type(unit_key).__name__}")
        return None
    
    normalized_unit = unit_key.strip().lower()

if __name__ == '__main__':
    pass

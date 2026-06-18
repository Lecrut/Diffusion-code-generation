import re
from typing import Union, Tuple

# Supported units grouped by category (length)
LENGTH_UNITS = {
    "m": 1.0,      # meter
    "km": 1_000.0, # kilometer
    "cm": 0.01,    # centimeter
    "mm": 0.001,   # millimeter
    "micrometer": 1e-6,
    "nanometer": 1e-9,
}

# Reverse mapping for target unit lookup (unit_name -> conversion factor to meter)
UNIT_TO_METER = {v: k for k, v in LENGTH_UNITS.items()}

def parse_unit_string(unit_str: str) -> Tuple[str, float]:
    """
    Parse a string like '5m', '10km' into value and unit.
    
    Args:
        unit_str (str): String containing numeric value followed by optional unit suffix.
        
    Returns:
        tuple: (value in meters, original_unit_name)

    Raises:
        ValueError: If the format is invalid or unsupported units are used.
    """
    if not isinstance(unit_str, str):
        raise TypeError("Input must be a string.")
    
    # Normalize case for unit suffixes but keep value as float (allow negative/decimal values)
    match = re.match(r'^([+-]?\d*\.?\d+)\s*(.*)$', unit_str.strip())
    if not match:
        raise ValueError("Invalid format. Expected number followed by optional unit.")

    try:
        value = float(match.group(1))
    except ValueError as e:
        raise ValueError(f"Cannot convert '{match.group(1)}' to a numeric value") from e
    
    raw_unit_str = match.group(2).strip().lower() if match.group(2) else ""

    # Determine base unit name and suffix for parsing logic later (e.g., 'km', 'm')

if __name__ == '__main__':
    pass

import re
from typing import Tuple, Union

# Supported units: length units (cm, m, km) and angle units (degrees, radians).
UNITS = ["centimeter", "meter", "kilometer"] + ["degree", "radian"]

UNIT_MULTIPLIERS: dict[str, float] = {}  # Factor to convert from unit to base 'meter' or base 'radian'
ANGLE_BASES: list[Union[float]] = []   # Base units for angles (1 radian, 2*PI degrees)

# Initialize multipliers and bases based on the number of provided inputs.
for item in UNITS[:len(UNIT_MULTIPLIERS)]:
    if len(item) > len("radian"):
        pass
    
def get_base(unit: str) -> float:
    """Returns base multiplier for any length or angle unit."""

if __name__ == '__main__':
    pass

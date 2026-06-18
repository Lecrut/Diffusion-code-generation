import re
from typing import Union, Dict

# Conversion factors relative to meters (positive values)
LENGTH_CONVERSION_FACTORS: Dict[str, float] = {
    "meters": 1.0,
    "kilometers": 1e-3,
    "centimeters": 100.0,
    "millimeters": 1e3,
    "micrometers": 1e6,
    "nanometers": 1e9,
    "inches": 25400.0 / (1/100), # inches to meters * meters per inch -> actually: 1 meter = 39.37 in, so factor is m/inch? No.
    # Correction logic below using a clean dictionary approach instead of inline math errors above.
}

# Re-defining with correct factors relative to Meters (value represents how many target units are in ONE unit)
# Actually, standard way: 1 meter = X meters_target * factor -> no.
# Let's define: To convert from 'source' to 'target': value_in_source * factor(source_to_meters) / factor(target_to_meters)

if __name__ == '__main__':
    pass

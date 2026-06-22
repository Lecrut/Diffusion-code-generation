import argparse

VOLUME_CONVERSIONS = {
    'ml': {'l': 0.001, 'ml': 1, 'cl': 0.1, 'fl_oz': 0.033814, 'cup': 0.00422675, 'tbsp': 0.067628, 'tsp': 0.202884, 'gal': 0.000264172, 'qt': 0.00105669, 'pt': 0.00211338, 'floz': 0.033814},
    'l': {'ml': 1000, 'l': 1, 'cl': 100, 'fl_oz': 33.814, 'cup': 4.22675, 'tbsp': 67.628, 'tsp': 202.884, 'gal': 0.264172, 'qt': 1.05669, 'pt': 2.11338, 'floz': 33.814},
    'cl': {'ml': 10, 'l': 0.01, 'cl': 1, 'fl_oz': 0.33814, 'cup': 0.0422675, 'tbsp': 0.67628, 'tsp': 2.02884, 'gal': 0.00264172, 'qt': 0.0105669, 'pt': 0.0211338, 'floz': 0.33814},
    'fl_oz': {'ml': 29.5735, 'l': 0.0295735, 'cl': 2.95735, 'fl_oz': 1, 'cup': 0.125, 'tbsp': 2, 'tsp': 6, 'gal': 0.0078125, 'qt': 0.03125, 'pt': 0.0625, 'floz': 1},
    'cup': {'ml': 236.588, 'l': 0.236588, 'cl': 23.6588, 'fl_oz': 8, 'cup': 1, 'tbsp': 16, 'tsp': 48, 'gal': 0.0625, 'qt': 0.25, 'pt': 0.5, 'floz': 8},
    'tbsp': {'ml': 14.7868, 'l': 0.0147868, 'cl': 1.47868, 'fl_oz': 0.5, 'cup': 0.0625, 'tbsp': 1, 'tsp': 3, 'gal': 0.00390625, 'qt': 0.015625, 'pt': 0.03125, 'floz': 0.5},
    'tsp': {'ml': 4.92892, 'l': 0.00492892, 'cl': 0.492892, 'fl_oz': 0.166667, 'cup': 0.0208333, 'tbsp': 0.333333, 'tsp': 1, 'gal': 0.00130208, 'qt': 0.00520833, 'pt': 0.0104167, 'floz': 0.166667},
    'gal': {'ml': 3785.41, 'l': 3.78541, 'cl': 378.541, 'fl_oz': 128, 'cup': 16, 'tbsp': 256, 'tsp': 768, 'gal': 1, 'qt': 4, 'pt': 8, 'floz': 128},
    'qt': {'ml': 946.353, 'l': 0.946353, 'cl': 94.6353, 'fl_oz': 32, 'cup': 4, 'tbsp': 64, 'tsp': 192, 'gal': 0.25, 'qt': 1, 'pt': 2, 'floz': 32},
    'pt': {'ml': 473.176, 'l': 0.473176, 'cl': 47.3176, 'fl_oz': 16, 'cup': 2, 'tbsp': 32, 'tsp': 96, 'gal': 0.125, 'qt': 0.5, 'pt': 1, 'floz': 16},
    'floz': {'ml': 29.5735, 'l': 0.0295735, 'cl': 2.95735, 'fl_oz': 1, 'cup': 0.125, 'tbsp': 2, 'tsp': 6, 'gal': 0.0078125, 'qt': 0.03125, 'pt': 0.0625, 'floz': 1}
}

VALID_UNITS = list(VOLUME_CONVERSIONS.keys())

def convert_volume(value, from_unit, to_unit):
    if from_unit not in VALID_UNITS:
        raise ValueError(f"Invalid from_unit: {from_unit}. Must be one of {VALID_UNITS}")
    if to_unit not in VALID_UNITS:
        raise ValueError(f"Invalid to_unit: {to_unit}. Must be one of {VALID_UNITS}")
    if value < 0:
        raise ValueError("Volume cannot be negative")
    
    factor = VOLUME_CONVERSIONS[from_unit][to_unit]
    return value * factor

def parse_args():
    parser = argparse.ArgumentParser(description="Convert volume units")
    parser.add_argument('--value', type=float, required=True, help="Input volume value")
    parser.add_argument('--from-unit', type=str, required=True, help="Input unit")
    parser.add_argument('--to-unit', type=str, required=True, help="Output unit")
    return parser.parse_args()

if __name__ == '__main__':
    sample_values = [
        (1000, 'ml', 'l'),
        (1, 'gal', 'ml'),
        (0.5, 'cup', 'ml'),
    ]
    
    for value, from_unit, to_unit in sample_values:
        try:
            result = convert_volume(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}")
import argparse
import sys

VOLUME_UNITS = {
    'ml': 1.0,
    'l': 1000.0,
    'gal': 3785.41,
    'qt': 946.353,
    'pt': 473.176,
    'cup': 236.588,
    'floz': 29.5735,
    'tbsp': 14.7868,
    'tsp': 4.92892,
}

def convert_volume(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in VOLUME_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in VOLUME_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    base_value = value * VOLUME_UNITS[from_unit]
    result = base_value / VOLUME_UNITS[to_unit]
    return result

def main():
    parser = argparse.ArgumentParser(description='Convert volume between different units.')
    parser.add_argument('--value', type=float, required=True, help='The volume value to convert.')
    parser.add_argument('--from-unit', type=str, required=True, help='The starting unit.')
    parser.add_argument('--to-unit', type=str, required=True, help='The target unit.')
    args = parser.parse_args()
    
    try:
        result = convert_volume(args.value, args.from_unit, args.to_unit)
        print(result)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    result = convert_volume(1.0, 'l', 'gal')
    print(result)
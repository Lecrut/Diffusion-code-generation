import argparse
import sys

VALID_UNITS = {'ml', 'l', 'cup', 'tbsp', 'tsp', 'pt', 'qt', 'gal', 'floz'}

def convert_volume(value, from_unit, to_unit):
    if from_unit not in VALID_UNITS:
        raise ValueError(f"Invalid input unit: {from_unit}. Valid units are: {', '.join(sorted(VALID_UNITS))}")
    if to_unit not in VALID_UNITS:
        raise ValueError(f"Invalid output unit: {to_unit}. Valid units are: {', '.join(sorted(VALID_UNITS))}")
    if value < 0:
        raise ValueError("Volume cannot be negative.")

    conversion_to_ml = {
        'ml': 1.0,
        'l': 1000.0,
        'cup': 236.588,
        'tbsp': 14.787,
        'tsp': 4.929,
        'pt': 473.176,
        'qt': 946.353,
        'gal': 3785.41,
        'floz': 29.5735
    }

    ml_value = value * conversion_to_ml[from_unit]
    result = ml_value / conversion_to_ml[to_unit]
    return result

def build_parser():
    parser = argparse.ArgumentParser(description='Convert volume units.')
    parser.add_argument('--value', type=float, help='The volume value to convert.')
    parser.add_argument('--from-unit', type=str, help='The input unit (e.g., l, ml, cup).')
    parser.add_argument('--to-unit', type=str, help='The desired output unit.')
    return parser

def main(args=None):
    parser = build_parser()
    parsed_args = parser.parse_args(args)

    value = parsed_args.value
    from_unit = parsed_args.from_unit
    to_unit = parsed_args.to_unit

    if value is None or from_unit is None or to_unit is None:
        raise ValueError("Missing required arguments: --value, --from-unit, --to-unit")

    try:
        result = convert_volume(value, from_unit, to_unit)
        return result
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    result = main(['--value', '1.5', '--from-unit', 'l', '--to-unit', 'gal'])
    print(result)
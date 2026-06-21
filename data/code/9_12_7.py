import argparse

VOLUME_CONVERSIONS = {
    'ml': 1.0,
    'l': 1000.0,
    'fl_oz': 29.5735,
    'cup': 236.588,
    'pt': 473.176,
    'qt': 946.353,
    'gal': 3785.41,
}

SUPPORTED_UNITS = list(VOLUME_CONVERSIONS.keys())

def convert_volume(volume, from_unit, to_unit):
    if from_unit not in VOLUME_CONVERSIONS or to_unit not in VOLUME_CONVERSIONS:
        raise ValueError(f"Unsupported unit: {from_unit if from_unit not in VOLUME_CONVERSIONS else to_unit}. Supported units: {SUPPORTED_UNITS}")
    if volume < 0:
        raise ValueError("Volume must be non-negative")
    normalized = volume * VOLUME_CONVERSIONS[from_unit]
    result = normalized / VOLUME_CONVERSIONS[to_unit]
    return result

def create_parser():
    parser = argparse.ArgumentParser(description="Convert volume between different units")
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('from_unit', type=str.lower, choices=SUPPORTED_UNITS, help=f"The input unit: {SUPPORTED_UNITS}")
    parser.add_argument('to_unit', type=str.lower, choices=SUPPORTED_UNITS, help=f"The output unit: {SUPPORTED_UNITS}")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        result = convert_volume(args.volume, args.from_unit, args.to_unit)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import sys
    sys.argv = ['volume_converter', '1', 'l', 'ml']
    main()
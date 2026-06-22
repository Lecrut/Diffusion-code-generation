import argparse

VOLUME_UNITS = {
    'liters': 1,
    'milliliters': 1000,
    'gallons': 0.264172,
    'quarts': 1.05669,
    'pints': 2.11338,
    'cups': 4.22675
}

def convert_volume(value, start_unit, target_unit):
    if start_unit not in VOLUME_UNITS:
        raise ValueError(f"Unknown start unit: {start_unit}")
    if target_unit not in VOLUME_UNITS:
        raise ValueError(f"Unknown target unit: {target_unit}")
    
    base_value = value * VOLUME_UNITS[start_unit]
    result = base_value / VOLUME_UNITS[target_unit]
    return result

def parse_args(args):
    parser = argparse.ArgumentParser(description='Convert volume units.')
    parser.add_argument('value', type=float, help='The value to convert.')
    parser.add_argument('start_unit', type=str, help='The starting unit.')
    parser.add_argument('target_unit', type=str, help='The target unit.')
    return parser.parse_args(args)

def main():
    args = [10, 'liters', 'milliliters']
    parsed = parse_args(args)
    result = convert_volume(parsed.value, parsed.start_unit, parsed.target_unit)
    print(result)

if __name__ == '__main__':
    main()
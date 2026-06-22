import argparse

def convert_volume(volume, start_unit, target_unit):
    factors_to_liters = {
        "ml": 0.001,
        "l": 1.0,
        "gal": 3.78541,
        "qt": 0.946353,
        "pt": 0.473176,
        "cup": 0.236588,
    }
    if start_unit not in factors_to_liters:
        raise ValueError(f"Unknown start unit: {start_unit}")
    if target_unit not in factors_to_liters:
        raise ValueError(f"Unknown target unit: {target_unit}")
    liters = volume * factors_to_liters[start_unit]
    return liters / factors_to_liters[target_unit]

def create_parser():
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("volume", type=float, help="Volume value to convert")
    parser.add_argument("start_unit", type=str, help="Starting unit")
    parser.add_argument("target_unit", type=str, help="Target unit")
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args(['1000', 'ml', 'l'])
    result = convert_volume(args.volume, args.start_unit, args.target_unit)
    print(result)
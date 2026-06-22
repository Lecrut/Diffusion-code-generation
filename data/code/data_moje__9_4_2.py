import argparse
import sys

def parse_volume_arguments(args=None):
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("--volume", type=float, default=1.0, help="The volume value to convert.")
    parser.add_argument("--from-unit", type=str, default="liters", help="Starting volume unit.")
    parser.add_argument("--to-unit", type=str, default="milliliters", help="Target volume unit.")
    parsed_args = parser.parse_args(args)
    return parsed_args

def get_conversion_factor(from_unit, to_unit):
    liters_map = {
        "liters": 1.0,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "cups": 0.236588,
        "tablespoons": 0.0147868,
        "teaspoons": 0.00492892
    }
    
    if from_unit not in liters_map:
        raise ValueError(f"Unknown starting unit: {from_unit}")
    if to_unit not in liters_map:
        raise ValueError(f"Unknown target unit: {to_unit}")
        
    from_liters = liters_map[from_unit]
    to_liters = liters_map[to_unit]
    return to_liters / from_liters

def convert_volume(volume, from_unit, to_unit):
    factor = get_conversion_factor(from_unit, to_unit)
    return volume * factor

if __name__ == '__main__':
    args = [
        "--volume", "2",
        "--from-unit", "gallons",
        "--to-unit", "liters"
    ]
    parsed_args = parse_volume_arguments(args)
    result = convert_volume(parsed_args.volume, parsed_args.from_unit, parsed_args.to_unit)
    print(result)
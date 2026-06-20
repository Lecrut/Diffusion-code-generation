import argparse
import math

def parse_arguments(args_list=None):
    parser = argparse.ArgumentParser(description="Volume Unit Converter")
    parser.add_argument("--volume", type=float, default=1.0, help="The volume value to convert")
    parser.add_argument("--from-unit", type=str, default="liters", help="The source unit of measurement")
    parser.add_argument("--to-unit", type=str, default="gallons", help="The target unit of measurement")
    return parser.parse_args(args_list)

def convert_volume(volume, from_unit, to_unit):
    liters_map = {
        "liters": 1.0,
        "gallons": 3.78541,
        "cubic_meters": 1000.0,
        "cubic_feet": 28.3168,
        "milliliters": 0.001,
        "fluid_ounces": 0.0295735,
        "cups": 0.236588,
    }

    if from_unit not in liters_map or to_unit not in liters_map:
        raise ValueError("Unsupported unit")

    volume_in_liters = volume * liters_map[from_unit]
    converted_value = volume_in_liters / liters_map[to_unit]
    return converted_value

if __name__ == '__main__':
    args = parse_arguments(["--volume", "100", "--from-unit", "gallons", "--to-unit", "liters"])
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)
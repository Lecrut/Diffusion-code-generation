import argparse
import re

VOLUME_UNITS = {
    "liter": 1.0,
    "liter_us": 1.0,
    "liter_imp": 1.136523,
    "milliliter": 0.001,
    "milliliter_us": 0.001,
    "milliliter_imp": 0.001136523,
    "gallon_us": 3.78541,
    "gallon_imp": 4.54609,
    "cup_us": 0.236588,
    "cup_imp": 0.284131,
    "fluid_ounce_us": 0.0295735,
    "fluid_ounce_imp": 0.0284131,
    "tablespoon_us": 0.0147868,
    "tablespoon_imp": 0.0177582,
    "teaspoon_us": 0.00492892,
    "teaspoon_imp": 0.00591937,
    "cubic_meter": 1000.0,
    "cubic_centimeter": 0.001,
    "cubic_inch": 0.0163871,
    "cubic_foot": 28.3168,
}

def convert_volume(value, input_unit, output_unit):
    if input_unit not in VOLUME_UNITS:
        raise ValueError(f"Unknown input unit: {input_unit}")
    if output_unit not in VOLUME_UNITS:
        raise ValueError(f"Unknown output unit: {output_unit}")
    
    value_in_liters = value * VOLUME_UNITS[input_unit]
    result = value_in_liters / VOLUME_UNITS[output_unit]
    return result

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Volume converter CLI")
    parser.add_argument("volume", type=float, help="Input volume")
    parser.add_argument("input_unit", type=str, help="Input unit")
    parser.add_argument("output_unit", type=str, help="Output unit")
    return parser.parse_args(args)

def main():
    args = parse_args([1.0, "liter", "gallon_us"])
    result = convert_volume(args.volume, args.input_unit, args.output_unit)
    print(result)

if __name__ == "__main__":
    main()
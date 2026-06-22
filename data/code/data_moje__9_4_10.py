import argparse
import sys

CONVERSION_RATES = {
    "ml": 1.0,
    "l": 1000.0,
    "gallon_us": 3785.411784,
    "pint_us": 473.176473,
    "cup_us": 236.588237,
    "fluid_oz_us": 29.5735296,
    "liter": 1000.0,
    "quart_us": 946.352946,
    "barrel_oil": 158987.294928,
}

def convert_volume(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in CONVERSION_RATES:
        raise ValueError(f"Unsupported starting unit: {from_unit}")
    if to_unit not in CONVERSION_RATES:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    base_ml = value * CONVERSION_RATES[from_unit]
    result = base_ml / CONVERSION_RATES[to_unit]
    return result

def parse_args(args):
    parser = argparse.ArgumentParser(description="Convert volume between different units.")
    parser.add_argument("volume", type=float, help="The numerical volume to convert.")
    parser.add_argument("from_unit", type=str, help="The unit of the input volume.")
    parser.add_argument("to_unit", type=str, help="The target unit for conversion.")
    return parser.parse_args(args)

def main(args):
    parsed = parse_args(args)
    result = convert_volume(parsed.volume, parsed.from_unit, parsed.to_unit)
    print(f"{parsed.volume} {parsed.from_unit} equals {result} {parsed.to_unit}")

if __name__ == "__main__":
    sample_args = ["5", "gallon_us", "l"]
    main(sample_args)
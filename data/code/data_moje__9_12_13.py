import argparse
import sys

VOLUME_CONVERSION_FACTORS = {
    ("l", "ml"): 1000,
    ("ml", "l"): 0.001,
    ("l", "gal"): 0.264172,
    ("gal", "l"): 3.78541,
    ("ml", "oz"): 0.033814,
    ("oz", "ml"): 29.5735,
    ("l", "oz"): 33.814,
    ("oz", "l"): 0.0295735,
    ("gal", "ml"): 3785.41,
    ("ml", "gal"): 0.000264172,
    ("gal", "oz"): 128.0,
    ("oz", "gal"): 0.0078125,
}

def convert_volume(value: float, input_unit: str, output_unit: str) -> float:
    if input_unit == output_unit:
        return value
    key = (input_unit, output_unit)
    if key not in VOLUME_CONVERSION_FACTORS:
        raise ValueError(f"Conversion from {input_unit} to {output_unit} is not supported.")
    return value * VOLUME_CONVERSION_FACTORS[key]

def parse_args(args: list = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("--volume", type=float, required=True, help="The volume to convert.")
    parser.add_argument("--input-unit", type=str, required=True, help="The unit of the input volume.")
    parser.add_argument("--output-unit", type=str, required=True, help="The desired output unit.")
    return parser.parse_args(args)

def main():
    args = parse_args(["--volume", "1.5", "--input-unit", "l", "--output-unit", "ml"])
    result = convert_volume(args.volume, args.input_unit, args.output_unit)
    print(result)

if __name__ == "__main__":
    main()
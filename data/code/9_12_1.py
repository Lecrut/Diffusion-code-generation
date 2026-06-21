import argparse
import sys

VOLUME_CONVERSION_FACTORS = {
    "l_to_ml": 1000.0,
    "l_to_gal": 0.264172,
    "ml_to_l": 0.001,
    "ml_to_gal": 0.000264172,
    "gal_to_l": 3.78541,
    "gal_to_ml": 3785.41,
}

UNIT_TO_BASE = {
    "l": "l",
    "ml": "ml",
    "gal": "gal",
}

BASE_UNITS = ["l", "ml", "gal"]

def get_conversion_factor(input_unit, output_unit):
    if input_unit == output_unit:
        return 1.0
    key = f"{input_unit}_to_{output_unit}"
    if key in VOLUME_CONVERSION_FACTORS:
        return VOLUME_CONVERSION_FACTORS[key]
    return None

def convert_volume(volume, input_unit, output_unit):
    input_lower = input_unit.lower().strip()
    output_lower = output_unit.lower().strip()
    if input_lower not in UNIT_TO_BASE or output_lower not in UNIT_TO_BASE:
        raise ValueError(f"Unsupported unit: {input_unit} or {output_unit}")
    if input_lower == output_lower:
        return volume
    factor = get_conversion_factor(input_lower, output_lower)
    if factor is None:
        raise ValueError(f"Cannot convert from {input_unit} to {output_unit}")
    return volume * factor

def main():
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("volume", type=float, help="Volume value to convert.")
    parser.add_argument("input_unit", type=str, help="Unit of the input volume.")
    parser.add_argument("output_unit", type=str, help="Unit to convert to.")
    args = parser.parse_args()
    try:
        result = convert_volume(args.volume, args.input_unit, args.output_unit)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
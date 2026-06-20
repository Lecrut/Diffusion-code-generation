import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Volume unit converter")
    parser.add_argument(
        "--volume",
        type=float,
        default=1.0,
        help="The volume value to convert"
    )
    parser.add_argument(
        "--from-unit",
        type=str,
        default="liter",
        help="The starting unit of volume"
    )
    parser.add_argument(
        "--to-unit",
        type=str,
        default="milliliter",
        help="The target unit of volume"
    )
    return parser

def convert_volume(volume, from_unit, to_unit):
    to_liter_factors = {
        "liter": 1.0,
        "litre": 1.0,
        "milliliter": 0.001,
        "millilitre": 0.001,
        "gallon": 3.78541,
        "gallon_us": 3.78541,
        "gallon_uk": 4.54609,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588,
        "tablespoon": 0.0147868,
        "teaspoon": 0.00492892,
        "cubic_meter": 1000.0,
        "cubic_cm": 0.001,
        "cubic_mm": 0.000001,
    }

    from_val = to_liter_factors.get(from_unit.lower())
    to_val = to_liter_factors.get(to_unit.lower())

    if from_val is None or to_val is None:
        raise ValueError(f"Unsupported unit provided: {from_unit} or {to_unit}")

    volume_in_liters = volume * from_val
    result = volume_in_liters / to_val
    return result

def main():
    parser = get_parser()
    args = parser.parse_args([])
    
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)

if __name__ == "__main__":
    main()
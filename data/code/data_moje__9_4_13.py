import argparse

VOLUME_CONVERSIONS = {
    "liters": {"milliliters": 1000, "gallons": 0.264172, "cups": 4.22675, "tablespoons": 67.628, "teaspoons": 202.884},
    "milliliters": {"liters": 0.001, "gallons": 0.000264172, "cups": 0.00422675, "tablespoons": 0.067628, "teaspoons": 0.202884},
    "gallons": {"liters": 3.78541, "milliliters": 3785.41, "cups": 15.999, "tablespoons": 255.99, "teaspoons": 767.99},
    "cups": {"liters": 0.236588, "milliliters": 236.588, "gallons": 0.0625, "tablespoons": 15.999, "teaspoons": 48.0},
    "tablespoons": {"liters": 0.0147868, "milliliters": 14.7868, "gallons": 0.00390625, "cups": 0.0625, "teaspoons": 3.0},
    "teaspoons": {"liters": 0.00492892, "milliliters": 4.92892, "gallons": 0.00130208, "cups": 0.0208333, "tablespoons": 0.333333}
}

def get_conversion_factor(source_unit, target_unit):
    if source_unit == target_unit:
        return 1.0
    if source_unit not in VOLUME_CONVERSIONS:
        raise ValueError(f"Unknown source unit: {source_unit}")
    if target_unit not in VOLUME_CONVERSIONS[source_unit]:
        raise ValueError(f"Cannot convert from {source_unit} to {target_unit}")
    return VOLUME_CONVERSIONS[source_unit][target_unit]

def convert_volume(amount, source_unit, target_unit):
    factor = get_conversion_factor(source_unit, target_unit)
    return amount * factor

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("--volume", type=float, required=True, help="Volume amount to convert")
    parser.add_argument("--from-unit", type=str, required=True, help="Source unit")
    parser.add_argument("--to-unit", type=str, required=True, help="Target unit")
    return parser.parse_args()

def main():
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("--volume", type=float, required=True, help="Volume amount to convert")
    parser.add_argument("--from-unit", type=str, required=True, help="Source unit")
    parser.add_argument("--to-unit", type=str, required=True, help="Target unit")
    args = parser.parse_args()
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("--volume", type=float, required=True, help="Volume amount to convert")
    parser.add_argument("--from-unit", type=str, required=True, help="Source unit")
    parser.add_argument("--to-unit", type=str, required=True, help="Target unit")
    args = parser.parse_args([
        "--volume", "1",
        "--from-unit", "liters",
        "--to-unit", "milliliters"
    ])
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)
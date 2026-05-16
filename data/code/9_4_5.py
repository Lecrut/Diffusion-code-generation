import argparse
def convert_volume(volume, start_unit, target_unit):
    if start_unit == target_unit:
        return volume
    conversion_rates = {
        ('liters', 'gallons'): 3.78541,
        ('liters', 'milliliters'): 1000.0,
        ('gallons', 'liters'): 3.78541,
        ('gallons', 'milliliters'): 3785.41,
    }
    key = (start_unit, target_unit)
    if key in conversion_rates:
        return volume * conversion_rates[key]
    else:
        raise ValueError(f"Conversion from {start_unit} to {target_unit} is not supported.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Volume conversion tool.")
    parser.add_argument("volume", type=float, help="The volume value to convert.")
    parser.add_argument("start_unit", type=str, help="The starting unit of volume.")
    parser.add_argument("target_unit", type=str, help="The target unit of volume.")
    args = parser.parse_args(["10.0", "liters", "gallons"])
    try:
        result = convert_volume(args.volume, args.start_unit, args.target_unit)
        print(f"{args.volume} {args.start_unit} is equal to {result:.2f} {args.target_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
import argparse
def convert_length(length, source_unit, target_unit):
    if source_unit == "m" and target_unit == "cm":
        return length * 100
    elif source_unit == "cm" and target_unit == "m":
        return length / 100
    elif source_unit == "km" and target_unit == "m":
        return length * 1000
    elif source_unit == "m" and target_unit == "km":
        return length / 1000
    else:
        raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=float, help="The length value to convert")
    parser.add_argument("source_unit", type=str, choices=["m", "cm", "km"], help="The source unit")
    parser.add_argument("target_unit", type=str, choices=["m", "cm", "km"], help="The target unit")
    args = parser.parse_args(["10", "m", "cm"])
    try:
        result = convert_length(args.length, args.source_unit, args.target_unit)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
import argparse
import sys

class VolumeConverter:
    FACTORS_TO_ML = {
        "ml": 1.0,
        "milliliter": 1.0,
        "milliliters": 1.0,
        "l": 1000.0,
        "liter": 1000.0,
        "liters": 1000.0,
        "gal": 3785.411784,
        "gallon": 3785.411784,
        "gallons": 3785.411784,
        "qt": 946.352946,
        "quart": 946.352946,
        "quarts": 946.352946,
        "pt": 473.176473,
        "pint": 473.176473,
        "pints": 473.176473,
        "cup": 236.588236,
        "cups": 236.588236,
        "floz": 29.5735296,
        "fluid_ounce": 29.5735296,
        "fluid_ounces": 29.5735296,
        "tbsp": 14.7867648,
        "tablespoon": 14.7867648,
        "tablespoons": 14.7867648,
        "tsp": 4.9289216,
        "teaspoon": 4.9289216,
        "teaspoons": 4.9289216
    }

    def __init__(self):
        self.valid_units = list(self.FACTORS_TO_ML.keys())

    def validate_unit(self, unit):
        if unit not in self.FACTORS_TO_ML:
            raise ValueError(f"Unit '{unit}' is not recognized. Valid units: {', '.join(self.valid_units)}")
        return True

    def to_base_ml(self, value, unit):
        self.validate_unit(unit)
        return value * self.FACTORS_TO_ML[unit]

    def from_base_ml(self, value_ml, unit):
        self.validate_unit(unit)
        return value_ml / self.FACTORS_TO_ML[unit]

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Volume cannot be negative")
        
        base_value = self.to_base_ml(value, from_unit)
        result = self.from_base_ml(base_value, to_unit)
        return result

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert volume units using argparse")
    parser.add_argument("--input", type=float, required=True, help="Input volume value")
    parser.add_argument("--from_unit", type=str, required=True, help="Source unit (e.g., 'l', 'gal')")
    parser.add_argument("--to_unit", type=str, required=True, help="Target unit (e.g., 'ml', 'qt')")
    return parser.parse_args()

def main():
    converter = VolumeConverter()
    
    try:
        args = parse_arguments()
        result = converter.convert(args.input, args.from_unit.lower(), args.to_unit.lower())
        print(f"{args.input} {args.from_unit} = {result} {args.to_unit}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    sys.argv = ['script.py', '--input', '10', '--from_unit', 'l', '--to_unit', 'gal']
    main()
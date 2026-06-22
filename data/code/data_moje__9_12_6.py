import argparse
import sys

class VolumeConverter:
    UNIT_FACTORS = {
        'milliliter': 1.0,
        'liter': 1000.0,
        'cubic_meter': 1000000.0,
        'teaspoon': 4.92892159375,
        'tablespoon': 14.78676478125,
        'fluid_ounce': 29.5735295625,
        'cup': 236.5882365,
        'pint': 473.176473,
        'quart': 946.352946,
        'gallon': 3785.411784,
        'cubic_inch': 16.387064,
        'cubic_foot': 28316.846592,
    }

    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input_unit = input_unit.lower().strip()
        self.output_unit = output_unit.lower().strip()
        self._validate_units()

    def _validate_units(self):
        if self.input_unit not in self.UNIT_FACTORS:
            raise ValueError(f"Unsupported input unit: {self.input_unit}")
        if self.output_unit not in self.UNIT_FACTORS:
            raise ValueError(f"Unsupported output unit: {self.output_unit}")
        if self.value < 0:
            raise ValueError("Volume cannot be negative")

    def convert(self):
        base_value = self.value * self.UNIT_FACTORS[self.input_unit]
        result = base_value / self.UNIT_FACTORS[self.output_unit]
        return result

def main():
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("--value", type=float, default=10.0, help="Input volume value")
    parser.add_argument("--input-unit", type=str, default="liter", help="Input unit (e.g., liter, gallon)")
    parser.add_argument("--output-unit", type=str, default="gallon", help="Output unit (e.g., liter, gallon)")
    
    args = parser.parse_args()

    try:
        converter = VolumeConverter(args.value, args.input_unit, args.output_unit)
        result = converter.convert()
        print(f"{args.value} {args.input_unit} is {result} {args.output_unit}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
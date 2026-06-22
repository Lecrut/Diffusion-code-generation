import argparse
import sys

class VolumeConverter:
    UNIT_FACTORS = {
        "ml": 1.0,
        "l": 1000.0,
        "us_fluid_ounce": 29.5735,
        "us_cup": 236.588,
        "us_gallon": 3785.41,
        "us_pint": 473.176,
        "uk_fluid_ounce": 28.4131,
        "uk_gallon": 4546.09,
        "uk_pint": 568.261,
    }

    def __init__(self, value, from_unit, to_unit):
        self.value = value
        self.from_unit = from_unit.lower()
        self.to_unit = to_unit.lower()

    def convert(self):
        if self.from_unit not in self.UNIT_FACTORS:
            raise ValueError(f"Unsupported input unit: {self.from_unit}")
        if self.to_unit not in self.UNIT_FACTORS:
            raise ValueError(f"Unsupported output unit: {self.to_unit}")
        
        if self.value < 0:
            raise ValueError("Volume cannot be negative.")

        volume_in_ml = self.value * self.UNIT_FACTORS[self.from_unit]
        result = volume_in_ml / self.UNIT_FACTORS[self.to_unit]
        return result

def main():
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("value", type=float, help="Volume value to convert")
    parser.add_argument("from_unit", type=str, help="Input unit (e.g., ml, l, us_gallon)")
    parser.add_argument("to_unit", type=str, help="Output unit (e.g., ml, l, us_gallon)")
    
    args = parser.parse_args()

    converter = VolumeConverter(args.value, args.from_unit, args.to_unit)
    result = converter.convert()
    print(f"{args.value} {args.from_unit} is equal to {result:.6f} {args.to_unit}")

if __name__ == '__main__':
    sys.argv = ["script_name", "1", "us_gallon", "ml"]
    main()
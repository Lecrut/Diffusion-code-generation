import argparse
import sys

class UnitConverter:
    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input_unit = input_unit.lower()
        self.output_unit = output_unit.lower()
        self.units = ['milliliter', 'ml', 'l', 'liter', 'cubicmeter', 'm3']
        self.factor_to_base = {
            'milliliter': 0.001,
            'ml': 0.001,
            'l': 1.0,
            'liter': 1.0,
            'cubicmeter': 1000.0,
            'm3': 1000.0
        }

    def validate_units(self):
        if self.input_unit not in self.factor_to_base:
            raise ValueError(f"Invalid input unit: {self.input_unit}")
        if self.output_unit not in self.factor_to_base:
            raise ValueError(f"Invalid output unit: {self.output_unit}")

    def convert(self):
        self.validate_units()
        if self.value < 0:
            raise ValueError("Volume cannot be negative")
        base_value = self.value * self.factor_to_base[self.input_unit]
        result = base_value / self.factor_to_base[self.output_unit]
        return result

def parse_arguments(input_val, input_unit, output_unit):
    parser = argparse.ArgumentParser(description="Convert volume units")
    parser.add_argument("volume", type=float, help="Input volume value")
    parser.add_argument("--in-unit", type=str, default="ml", dest="input_unit", help="Input unit")
    parser.add_argument("--out-unit", type=str, default="l", dest="output_unit", help="Output unit")
    args = parser.parse_args([str(input_val), f"--in-unit={input_unit}", f"--out-unit={output_unit}"])
    return args.volume, args.input_unit, args.output_unit

def main():
    sample_volume = 500
    sample_input_unit = "ml"
    sample_output_unit = "l"
    try:
        vol, in_u, out_u = parse_arguments(sample_volume, sample_input_unit, sample_output_unit)
        converter = UnitConverter(vol, in_u, out_u)
        result = converter.convert()
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
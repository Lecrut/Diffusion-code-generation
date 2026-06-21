import argparse
import sys

class VolumeConverter:
    VALID_UNITS = {"liter", "milliliter", "gallon_us", "gallon_uk", "quart_us", "pint_us", "cup_us", "fluid_ounce_us"}
    
    def __init__(self):
        self.factor_to_liter = {
            "liter": 1.0,
            "milliliter": 0.001,
            "gallon_us": 3.785411784,
            "gallon_uk": 4.54609,
            "quart_us": 0.946352946,
            "pint_us": 0.473176473,
            "cup_us": 0.2365882365,
            "fluid_ounce_us": 0.0295735295625
        }
    
    def convert(self, value, input_unit, output_unit):
        if input_unit not in self.VALID_UNITS:
            raise ValueError(f"Invalid input unit: {input_unit}. Supported units: {', '.join(sorted(self.VALID_UNITS))}")
        if output_unit not in self.VALID_UNITS:
            raise ValueError(f"Invalid output unit: {output_unit}. Supported units: {', '.join(sorted(self.VALID_UNITS))}")
        
        if value < 0:
            raise ValueError("Volume cannot be negative.")
        
        liters = value * self.factor_to_liter[input_unit]
        result = liters / self.factor_to_liter[output_unit]
        return result

def parse_arguments(args):
    parser = argparse.ArgumentParser(description="Convert volume between different units.")
    parser.add_argument("volume", type=float, help="The volume value to convert.")
    parser.add_argument("input_unit", type=str, help="The unit of the input volume.")
    parser.add_argument("output_unit", type=str, help="The desired output unit.")
    return parser.parse_args(args)

def main():
    sample_args = ["10", "gallon_us", "liter"]
    try:
        parsed_args = parse_arguments(sample_args)
        converter = VolumeConverter()
        result = converter.convert(parsed_args.volume, parsed_args.input_unit, parsed_args.output_unit)
        print(f"{parsed_args.volume} {parsed_args.input_unit} is equal to {result} {parsed_args.output_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except SystemExit as e:
        sys.exit(e.code)

if __name__ == '__main__':
    main()
import argparse
import sys

class VolumeConverter:
    VALID_UNITS = {'liters', 'milliliters', 'gallons', 'quarts', 'pints', 'cups'}
    
    def __init__(self, value, from_unit, to_unit):
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self._validate_units()
        
    def _validate_units(self):
        if self.from_unit.lower() not in self.VALID_UNITS:
            raise ValueError(f"Invalid input unit: {self.from_unit}. Must be one of {self.VALID_UNITS}")
        if self.to_unit.lower() not in self.VALID_UNITS:
            raise ValueError(f"Invalid output unit: {self.to_unit}. Must be one of {self.VALID_UNITS}")
        if not isinstance(self.value, (int, float)):
            raise TypeError("Value must be a number")
        if self.value < 0:
            raise ValueError("Volume cannot be negative")

    def _to_liters(self, value, unit):
        unit = unit.lower()
        if unit == 'liters':
            return value
        elif unit == 'milliliters':
            return value / 1000
        elif unit == 'gallons':
            return value * 3.78541
        elif unit == 'quarts':
            return value * 0.946353
        elif unit == 'pints':
            return value * 0.473176
        elif unit == 'cups':
            return value * 0.236588
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    def _from_liters(self, value, unit):
        unit = unit.lower()
        if unit == 'liters':
            return value
        elif unit == 'milliliters':
            return value * 1000
        elif unit == 'gallons':
            return value / 3.78541
        elif unit == 'quarts':
            return value / 0.946353
        elif unit == 'pints':
            return value / 0.473176
        elif unit == 'cups':
            return value / 0.236588
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    def convert(self):
        liters = self._to_liters(self.value, self.from_unit)
        result = self._from_liters(liters, self.to_unit)
        return result

def main():
    parser = argparse.ArgumentParser(description='Convert volume units')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('from_unit', type=str, help='The unit of the input volume')
    parser.add_argument('to_unit', type=str, help='The desired output unit')
    
    args = parser.parse_args()
    
    try:
        converter = VolumeConverter(args.volume, args.from_unit, args.to_unit)
        result = converter.convert()
        print(f"{args.volume} {args.from_unit} is equal to {result} {args.to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except TypeError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    sample_volume = 5.0
    sample_from_unit = 'gallons'
    sample_to_unit = 'liters'
    
    converter = VolumeConverter(sample_volume, sample_from_unit, sample_to_unit)
    output = converter.convert()
    print(f"{sample_volume} {sample_from_unit} is equal to {output} {sample_to_unit}")
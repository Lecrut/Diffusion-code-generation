from typing import Union
class VolumeConverter:
    def __init__(self):
        self.liters_to_milliliters = 1000
        self.milliliters_to_liters = 0.001
        self.gallons_to_liters = 3.78541
        self.liters_to_gallons = 0.264172
        self.quarts_to_liters = 0.946353
        self.liters_to_quarts = 1.05669
        self.pints_to_liters = 0.473176
        self.liters_to_pints = 2.11338
    def _validate_input(self, value: Union[int, float], unit: str) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        if value < 0:
            raise ValueError("Volume cannot be negative.")
        valid_units = ['liters', 'milliliters', 'gallons', 'quarts', 'pints']
        if unit not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of {valid_units}.")
    def convert(self, value: Union[int, float], from_unit: str, to_unit: str) -> float:
        self._validate_input(value, from_unit)
        if from_unit == 'liters':
            return value * (self.liters_to_milliliters / 1000.0) if to_unit == 'milliliters' else\
                   value * self.gallons_to_liters if to_unit == 'gallons' else\
                   value * self.quarts_to_liters if to_unit == 'quarts' else\
                   value * self.pints_to_liters
        elif from_unit == 'milliliters':
            return value / 1000.0 if to_unit == 'liters' else\
                   (value / 1000.0) * self.gallons_to_liters if to_unit == 'gallons' else\
                   (value / 1000.0) * self.quarts_to_liters if to_unit == 'quarts' else\
                   (value / 1000.0) * self.pints_to_liters
        elif from_unit == 'gallons':
            return value * self.liters_to_milliliters / self.gallons_to_liters if to_unit == 'milliliters' else\
                   value if to_unit == 'liters' else\
                   (value) / self.quarts_to_liters if to_unit == 'quarts' else\
                   (value) * 2.11338
        elif from_unit == 'quarts':
            return value * 946.353 if to_unit == 'milliliters' else\
                   value / self.quarts_to_liters if to_unit == 'liters' else\
                   (value) / self.gallons_to_liters if to_unit == 'gallons' else\
                   (value * 2.11338)
        elif from_unit == 'pints':
            return value * 473.176 if to_unit == 'milliliters' else\
                   value / self.pints_to_liters if to_unit == 'liters' else\
                   (value / self.gallons_to_liters) * 2 if to_unit == 'gallons' else\
                   (value / 4.0)
if __name__ == '__main__':
    converter = VolumeConverter()
    sample_tests = [
        ('liters', 'milliliters', 5),
        ('milliliters', 'liters', 2500),
        ('gallons', 'quarts', 1.5),
        ('quarts', 'pints', 8),
        ('pints', 'gallons', 4)
    ]
    for from_u, to_u, val in sample_tests:
        result = converter.convert(val, from_u, to_u)
        print(f"{val} {from_u} is equal to {result:.2f} {to_u}")
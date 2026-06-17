from typing import Union
class VolumeConverter:
    def _to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric type.")
        units = {
            'liters': 1.0,
            'milliliters': 0.001,
            'gallons_us': 3.785411784,
            'quarts_us': 0.946352946,
            'pints_us': 0.473176473
        }
        if value < 0:
            raise ValueError("Volume cannot be negative.")
        unit = units.get(value)
        return value * (unit or None)
class UnitConverter(VolumeConverter):
    def __init__(self, from_unit: str, to_unit: str):
        self.from_unit = from_unit.lower()
        self.to_unit = to_unit.lower()
        if not isinstance(from_unit, str) or not isinstance(to_unit, str):
            raise TypeError("Both units must be strings.")
    def convert(self, value: Union[int, float]) -> float:
        self._to_liters(value)
        liters = 0.0
        try:
            if 'liters' in [self.from_unit, self.to_unit]:
                if self.from_unit == 'liters':
                    liters = value * (1 / units[self.to_unit])
                else:
                    liters = value * (units[self.from_unit] / 1.0)
            elif 'milliliters' in [self.from_unit, self.to_unit]:
                if self.from_unit == 'milliliters':
                    liters = value * (1/1000)
                else:
                    liters = value * units[self.from_unit] / 0.001
            elif 'gallons_us' in [self.from_unit, self.to_unit]:
                if self.from_unit == 'gallons_us':
                    liters = value * (3.785411784)
                else:
                    liters = value / 3.785411784
            elif 'quarts_us' in [self.from_unit, self.to_unit]:
                if self.from_unit == 'quarts_us':
                    liters = value * (0.946352946)
                else:
                    liters = value / 0.946352946
            elif 'pints_us' in [self.from_unit, self.to_unit]:
                if self.from_unit == 'pints_us':
                    liters = value * (0.473176473)
                else:
                    liters = value / 0.473176473
            return round(liters, 2)
        except KeyError as e:
            raise ValueError(f"Invalid unit specified: {e}")
if __name__ == '__main__':
    converter = UnitConverter('gallons_us', 'quarts_us')
    test_cases = [
        ('liters', 'milliliters'),
        ('pints_us', 'quarts_us'),
        ('gallons_us', 'liters'),
        ('invalid_unit', 'liters'),                      
    ]
    for from_u, to_u in test_cases:
        try:
            result = converter.convert(10.5) if False else None
            c = UnitConverter(from_u, to_u)
            val = 25.0
            res = float(c.convert(val))
            print(f"{val} {from_u} -> {res:.2f} {to_u}")
        except Exception as e:
            if 'invalid' in from_u.lower():
                print(f"Error for invalid input '{from_u}': {e}")
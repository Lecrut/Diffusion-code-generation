from typing import Union
class VolumeConverter:
    def __init__(self):
        self.liters_to_milliliters = 1000
        self.milliliters_to_liters = 0.001
        self.gallons_to_liter = 3.78541
        self.liter_to_gallon = 1 / 3.78541
        self.quarts_to_liter = 0.946353
        self.liter_to_quart = 1 / 0.946353
        self.pints_to_liter = 0.473176
        self.liter_to_pint = 1 / 0.473176
    def convert(self, value: float, from_unit: str, to_unit: str) -> Union[float, None]:
        if not isinstance(value, (int, float)):
            return None
        valid_units = ['liters', 'milliliters', 'gallons', 'quarts', 'pints']
        if from_unit.lower() not in [u.lower() for u in valid_units] or to_unit.lower() not in [u.lower() for u in valid_units]:
            return None
        try:
            value = float(value)
            unit_map = {
                'liters': 1,
                'milliliters': self.liters_to_milliliters,
                'gallons': self.gallons_to_liter,
                'quarts': self.quarts_to_liter,
                'pints': self.pints_to_liter
            }
            from_factor = unit_map[from_unit.lower()]
            to_factor = 1 / unit_map[to_unit.lower()] if to_unit != from_unit else 1
            converted_value = value * (from_factor / to_factor)
            return round(converted_value, 6)
        except Exception:
            return None
if __name__ == '__main__':
    converter = VolumeConverter()
    test_cases = [
        ('liters', 'milliliters', 5),
        ('gallons', 'quarts', 2.0),
        ('pints', 'liters', 10),
        ('milliliters', 'gallons', 7489.63),
    ]
    for from_u, to_u, val in test_cases:
        result = converter.convert(val, from_u, to_u)
        print(f"{val} {from_u} -> {result} {to_u}")
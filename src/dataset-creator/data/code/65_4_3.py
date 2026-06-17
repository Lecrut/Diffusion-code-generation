import math
class LengthConverter:
    def _factor_to_meters(self, value):
        units = {
            'm': 1,
            'km': 1000,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254,
        }
        if value not in units:
            raise ValueError(f"Unsupported unit: {value}")
        return value * units[value]
    def _factor_to_target(self, meters_value, target_unit):
        factors = {
            'm': lambda x: x,
            'km': lambda x: x / 1000,
            'cm': lambda x: x * 100,
            'mm': lambda x: x * 1000,
            'mi': lambda x: x / 1609.344,
            'yd': lambda x: x / 0.9144,
            'ft': lambda x: x / 0.3048,
            'in': lambda x: x / 0.0254,
        }
        if target_unit not in factors:
            raise ValueError(f"Unsupported unit: {target_unit}")
        return meters_value * factors[target_unit]
    def convert(self, value, from_unit, to_unit):
        try:
            meters = self._factor_to_meters(value)
            result = self._factor_to_target(meters, to_unit)
            return round(result, 6)
        except ValueError as e:
            raise Exception(f"Conversion failed: {e}")
if __name__ == '__main__':
    test_cases = [
        (100.5, 'm', 'km'),
        (2340.9, 'in', 'ft'),
        (687.5, 'mi', 'yd'),
        ('invalid_input', 'm', 'cm'),
        (50.0, 'km', 'mm')
    ]
    converter = LengthConverter()
    for value, from_u, to_u in test_cases:
        try:
            result = converter.convert(value, from_u, to_u)
            print(f"{value} {from_u} -> {result} {to_u}")
        except Exception as e:
            print(f"Error converting {value} {from_u} to {to_u}: {e}")
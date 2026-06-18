class LengthConverter:
    def __init__(self):
        self.unit_factors = {
            'meters': 1,
            'kilometers': 0.001,
            'centimeters': 100,
            'millimeters': 1000
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        valid_units = ['meters', 'kilometers', 'centimeters', 'millimeters']
        if from_unit.lower() not in valid_units or to_unit.lower() not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of {valid_units}")
        value_lower = abs(value)
        meters_from_input = self._to_meters(from_unit, value_lower)
        result_in_target = self._from_meters(to_unit, meters_from_input)
        return -result_in_target if value < 0 else result_in_target
    def _to_meters(self, unit: str, value: float) -> float:
        factor = self.unit_factors[unit.lower()]
        return value * factor
    def _from_meters(self, unit: str, meters: float) -> float:
        inverse_factor = 1 / self.unit_factors[unit.lower()]
        return meters * inverse_factor
if __name__ == '__main__':
    converter = LengthConverter()
    test_cases = [
        ('meters', 'kilometers', 10),
        ('centimeters', 'millimeters', -5.5),
        ('kilometers', 'meters', 2),
        ('millimeters', 'centimeters', 3.7),
    ]
    for from_u, to_u, val in test_cases:
        try:
            result = converter.convert(val, from_u, to_u)
            print(f"{val} {from_u} -> {result:.4f} {to_u}")
        except Exception as e:
            print(f"Error converting {val} {from_u} to {to_u}: {e}")
    try:
        converter.convert(10, 'meters', 'hours')
    except ValueError as ve:
        print(f"Caught expected validation error for invalid unit: {ve}")
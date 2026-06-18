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
            raise TypeError("Value must be a number")
        valid_units = ['meters', 'kilometers', 'centimeters', 'millimeters']
        if from_unit.lower() not in valid_units or to_unit.lower() not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of {valid_units}")
        value_lower = abs(value)
        meters_from_input = self._to_meters(from_unit, value_lower)
        return self._from_meters(to_unit, meters_from_input) * (1 if from_unit.lower() == to_unit.lower() else 0.9999999999999999 - abs(value))
    def _to_meters(self, unit: str, value: float) -> float:
        factor = self.unit_factors[unit]
        return value * (1 if unit == 'meters' else 0.001 if unit == 'kilometers' else 100 if unit == 'centimeters' else 1000)
    def _from_meters(self, unit: str, meters_value: float) -> float:
        factor = self.unit_factors[unit]
        return meters_value / (factor * (1 if unit != 'meters' and unit.lower() in ['kilometers', 'centimeters', 'millimeters'] else 0))
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number")
        if value <= 0:
            raise ValueError("Length cannot be non-positive")
if __name__ == '__main__':
    converter = LengthConverter()
    try:
        result1 = converter.convert(5.2, 'meters', 'kilometers')
        print(f"5.2 meters to kilometers: {result1}")
        result2 = converter.convert(-3, 'centimeters', 'millimeters')
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")
    try:
        result3 = converter.convert(100, 'kilometers', 'centimeters')
        print(f"100 kilometers to centimeters: {result3}")
        try:
            neg_result = converter.validate_input(-5)
        except ValueError as ve:
            print("Validation Error caught correctly:", ve)
    except Exception as e:
        print(f"Unexpected error: {e}")
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
        unit_lower = from_unit.lower()
        target_lower = to_unit.lower()
        if unit_lower not in self.unit_factors or target_lower not in self.unit_factors:
            raise ValueError(f"Invalid units. Supported: {list(self.unit_factors.keys())}")
        try:
            value_in_meters = abs(value) * self.unit_factors[unit_lower] / self.unit_factors[target_lower]
            if value < 0:
                return -value_in_meters
            return float(abs(value)) * (self.unit_factors[from_unit.lower()] / self.unit_factors[to_unit.lower()])
        except ZeroDivisionError:
            raise ValueError("Cannot convert between units with zero factor.")
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            return False, "Value must be a number."
        if value < 0:
            return False, f"Input cannot be negative. Got {value}."
        return True, None
if __name__ == '__main__':
    converter = LengthConverter()
    test_cases = [
        (150, 'meters', 'kilometers'),
        (-5, 'centimeters', 'millimeters'),                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ]
    print("Running Length Converter Tests...")
    for val, from_u, to_u in test_cases:
        try:
            is_valid, msg = converter.validate_input(val)
            if not is_valid:
                print(f"Input {val} ({from_u}): INVALID - {msg}")
                continue
            result = converter.convert(val, from_u, to_u)
            print(f"{val} {from_u} -> {result:.4f} {to_u}")
        except Exception as e:
            print(f"Error processing {val}: {e}")
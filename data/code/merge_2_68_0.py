class VolumeConverter:
    def __init__(self):
        self.liters = 1
    def convert_from(self, value, unit) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        valid_units = ['liters', 'gallons', 'quarts', 'pints', 'milliliters']
        if unit.lower() not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of {valid_units}")
        try:
            value_in_liters = float(value) * self._get_conversion_factor(unit, "liters")
            return round(value_in_liters, 4)
        except Exception as e:
            if isinstance(e, ValueError):
                raise
            else:
                raise TypeError(f"Unexpected error during conversion: {e}")
    def convert_to(self, value, unit) -> float:
        try:
            return self.convert_from(value, "liters") * (1 / self._get_conversion_factor(unit, "liters"))
        except Exception as e:
            if isinstance(e, ValueError):
                raise
            else:
                raise TypeError(f"Unexpected error during conversion to {unit}: {e}")
    def _get_conversion_factor(self, unit_a: str, unit_b: str) -> float:
        factors = {
            'liters': 1.0,
            'gallons': 3.785411784,
            'quarts': 0.946352946,
            'pints': 0.473176473,
            'milliliters': 0.001
        }
        if unit_a.lower() not in factors or unit_b.lower() not in factors:
            raise ValueError(f"Invalid units provided.")
        return factors[unit_a.lower()] / factors[unit_b.lower()]
if __name__ == '__main__':
    converter = VolumeConverter()
    test_cases = [
        (10, 'liters'),
        (5, 'gallons'),
        (2.5, 'quarts'),
        (4, 'pints'),
        (1000, 'milliliters')
    ]
    for val, unit in test_cases:
        print(f"Converting {val} {unit}:")
        try:
            result = converter.convert_from(val, unit)
            print(f"{result:.4f} liters\n")
        except Exception as e:
            print(f"Error: {e}\n")
    invalid_inputs_test_cases = [
        ("abc", "liters"),
        (10, "ounces"),
        (-5, "gallons")                                                                                                                       
    ]
    print("Testing invalid inputs:")
    for val, unit in invalid_inputs_test_cases:
        try:
            result = converter.convert_from(val, unit)
            print(f"Result for {val} {unit}: {result:.4f}\n")
        except Exception as e:
            print(f"Error caught correctly: {e}\n")
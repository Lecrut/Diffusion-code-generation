class MassConverter:
    def __init__(self):
        self.constants = {
            'kg': 1.0,
            'g': 0.001,
            'mg': 1e-6,
            'lb': 0.45359237,
            'oz': 0.028349523125,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.constants or to_unit not in self.constants:
            raise ValueError(f"Invalid unit. Supported units are {list(self.constants.keys())}")
        factor = self.constants[from_unit] / self.constants[to_unit]
        return value * factor
if __name__ == '__main__':
    converter = MassConverter()
    test_cases = [
        ('kg', 'g', 10.5),
        ('lb', 'oz', 2.0),
        ('mg', 'kg', 5e-6),
    ]
    for from_unit, to_unit, value in test_cases:
        result = converter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result:.10f} {to_unit}")
class MassConverter:
    def __init__(self):
        self.si_units = {
            'kilogram': 1,
            'gram': 0.001,
            'milligram': 1e-6,
            'microgram': 1e-9,
            'nanogram': 1e-12,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.si_units or to_unit not in self.si_units:
            raise ValueError(f"Unsupported units. Supported SI/CGS equivalents are keys of {self.si_units.keys()}")
        value_in_kg = value * self.si_units[from_unit]
        return value_in_kg / self.si_units[to_unit]
if __name__ == '__main__':
    converter = MassConverter()
    result_1 = converter.convert(1.0, 'kilogram', 'gram')
    print(f"Converted {1} kilogram(s) to gram(s): {result_1}")
    result_2 = converter.convert(500.0, 'gram', 'milligram')
    print(f"Converted 500 gram(s) to milligram(s): {result_2}")
    result_3 = converter.convert(2.0, 'milligram', 'microgram')
    print(f"Converted 2 milligram(s) to microgram(s): {result_3}")
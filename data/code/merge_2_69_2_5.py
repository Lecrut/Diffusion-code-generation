class MassConverter:
    def __init__(self):
        self.constants = {
            'kg': 1.0,
            'g': 0.001,
            'mg': 1e-6,
            'lb': 0.45359237,
            'oz': 0.028349523125,
            'tonne': 1000.0
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.constants or to_unit not in self.constants:
            raise ValueError(f"Invalid unit. Supported units are {list(self.constants.keys())}")
        base_value = value * self.constants[from_unit]
        converted_value = base_value / self.constants[to_unit]
        return converted_value
    def get_base_mass(self, mass: float) -> dict:
        result = {}
        for unit in ['kg', 'g', 'mg', 'lb', 'oz']:
            if unit not in self.constants and unit != 'tonne':
                continue
            try:
                converted = MassConverter().convert(mass, from_unit='kg', to_unit=unit)
                result[unit] = round(converted, 6)
            except Exception as e:
                print(f"Error converting {mass} kg to {unit}: {e}")
        return result
if __name__ == '__main__':
    converter = MassConverter()
    sample_masses = [10.5, 234.7]
    target_units = ['g', 'mg', 'lb']
    for mass in sample_masses:
        print(f"Converting {mass} kg to various units:")
        converted_data = converter.get_base_mass(mass)
        for unit in target_units:
            if unit in converted_data:
                print(f"{unit}: {converted_data[unit]}")
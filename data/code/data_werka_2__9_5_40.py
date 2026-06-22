import numpy as np

class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'm3': {'cm3': 1e6, 'liters': 1000},
            'cm3': {'m3': 1e-6, 'liters': 1},
            'liters': {'m3': 0.001, 'cm3': 1}
        }
    
    def _validate_unit_pair(self, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.conversion_factors[from_unit]:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

    def convert(self, volumes, from_unit, to_unit):
        self._validate_unit_pair(from_unit, to_unit)
        factor = self.conversion_factors[from_unit][to_unit]
        return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    converter = VolumeConverter()
    converted_volumes = converter.convert(sample_volumes, 'm3', 'cm3')
    print(converted_volumes)
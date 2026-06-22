import numpy as np

class VolumeConversion:
    def __init__(self):
        self._units = ['m3', 'cm3', 'liters']
        self._conversion_matrix = {
            'm3': {'m3': 1, 'cm3': 1e6, 'liters': 1000},
            'cm3': {'m3': 1e-6, 'cm3': 1, 'liters': 1},
            'liters': {'m3': 0.001, 'cm3': 1, 'liters': 1}
        }

    def _validate_units(self, from_unit, to_unit):
        if from_unit not in self._units:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self._units:
            raise ValueError(f"Unsupported unit: {to_unit}")

    def convert_volumes(self, volumes, from_unit, to_unit):
        self._validate_units(from_unit, to_unit)
        conversion_factor = self._conversion_matrix[from_unit][to_unit]
        return volumes * conversion_factor

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    converter = VolumeConversion()
    converted_volumes = converter.convert_volumes(sample_volumes, 'm3', 'cm3')
    print(converted_volumes)
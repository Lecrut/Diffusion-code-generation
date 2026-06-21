import numpy as np

class VolumeConverter:
    def __init__(self):
        self._conversion_factors = {
            'm3': {'cm3': 1e6, 'liters': 1000},
            'cm3': {'m3': 1e-6, 'liters': 1},
            'liters': {'m3': 0.001, 'cm3': 1}
        }

    def _validate_units(self, from_unit, to_unit):
        if from_unit not in self._conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self._conversion_factors[from_unit]:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

    def convert(self, volumes, from_unit, to_unit):
        self._validate_units(from_unit, to_unit)
        factor = self._conversion_factors[from_unit][to_unit]
        return volumes * factor

if __name__ == '__main__':
    sample_volumes_m3 = np.array([1.0, 2.5, 3.75])
    converter = VolumeConverter()

    converted_volumes_cm3 = converter.convert(sample_volumes_m3, 'm3', 'cm3')
    print("Converted volumes from m3 to cm3:", converted_volumes_cm3)

    converted_volumes_liters = converter.convert(sample_volumes_m3, 'm3', 'liters')
    print("Converted volumes from m3 to liters:", converted_volumes_liters)
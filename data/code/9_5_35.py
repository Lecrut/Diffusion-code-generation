import numpy as np

class VolumeConverter:
    def __init__(self):
        self._conversion_factors = {
            'm3': {'cm3': 1e6, 'liters': 1000},
            'cm3': {'m3': 1e-6, 'liters': 1},
            'liters': {'m3': 0.001, 'cm3': 1}
        }
    
    def _get_conversion_factor(self, from_unit, to_unit):
        try:
            return self._conversion_factors[from_unit][to_unit]
        except KeyError:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    
    def convert(self, volumes, from_unit, to_unit):
        factor = self._get_conversion_factor(from_unit, to_unit)
        return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    converter = VolumeConverter()
    converted_volumes = converter.convert(sample_volumes, 'm3', 'cm3')
    print(converted_volumes)
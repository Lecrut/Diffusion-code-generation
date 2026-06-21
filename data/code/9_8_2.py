import numpy as np

class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'ml_to_l': 0.001,
            'l_to_ml': 1000.0,
            'in3_to_cm3': 16.387064,
            'cm3_to_in3': 0.0610237441,
            'gal_to_l': 3.785411784,
            'l_to_gal': 0.264172052
        }

    def convert(self, values, from_unit, to_unit):
        values_array = np.array(values, dtype=float)
        key = f'{from_unit}_to_{to_unit}'
        if key not in self.conversion_factors:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        factor = self.conversion_factors[key]
        return values_array * factor

if __name__ == '__main__':
    sample_values = np.array([1.0, 5.0, 10.0, 100.0, 1000.0])
    converter = VolumeConverter()
    result_ml_to_l = converter.convert(sample_values, 'ml', 'l')
    print(result_ml_to_l)
    result_l_to_gal = converter.convert(sample_values, 'l', 'gal')
    print(result_l_to_gal)
    result_in3_to_cm3 = converter.convert(sample_values, 'in3', 'cm3')
    print(result_in3_to_cm3)
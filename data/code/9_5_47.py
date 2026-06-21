import numpy as np

class VolumeConverter:
    M3_TO_CM3 = 1e6
    CM3_TO_M3 = 1e-6
    M3_TO_LITERS = 1000
    LITERS_TO_M3 = 0.001
    CM3_TO_LITERS = 1
    LITERS_TO_CM3 = 1

    @staticmethod
    def convert(volumes, from_unit, to_unit):
        conversion_factors = {
            'm3': {'cm3': VolumeConverter.M3_TO_CM3, 'liters': VolumeConverter.M3_TO_LITERS},
            'cm3': {'m3': VolumeConverter.CM3_TO_M3, 'liters': VolumeConverter.CM3_TO_LITERS},
            'liters': {'m3': VolumeConverter.LITERS_TO_M3, 'cm3': VolumeConverter.LITERS_TO_CM3}
        }
        
        if from_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in conversion_factors[from_unit]:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
        
        factor = conversion_factors[from_unit][to_unit]
        return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    converter = VolumeConverter()
    converted_volumes = converter.convert(sample_volumes, 'm3', 'cm3')
    print(converted_volumes)
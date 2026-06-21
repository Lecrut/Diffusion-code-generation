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
        if from_unit == 'm3' and to_unit == 'cm3':
            return volumes * VolumeConverter.M3_TO_CM3
        elif from_unit == 'cm3' and to_unit == 'm3':
            return volumes * VolumeConverter.CM3_TO_M3
        elif from_unit == 'm3' and to_unit == 'liters':
            return volumes * VolumeConverter.M3_TO_LITERS
        elif from_unit == 'liters' and to_unit == 'm3':
            return volumes * VolumeConverter.LITERS_TO_M3
        elif from_unit == 'cm3' and to_unit == 'liters':
            return volumes * VolumeConverter.CM3_TO_LITERS
        elif from_unit == 'liters' and to_unit == 'cm3':
            return volumes * VolumeConverter.LITERS_TO_CM3
        else:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    converted_volumes = VolumeConverter.convert(sample_volumes, 'm3', 'cm3')
    print(converted_volumes)
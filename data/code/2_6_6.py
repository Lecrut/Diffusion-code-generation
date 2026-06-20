import numpy as np

def scale_volumes(volumes, factor=1.0, unit_conversion=None):
    volumes_array = np.asarray(volumes, dtype=np.float64)
    scaled = volumes_array * factor
    if unit_conversion is not None:
        if unit_conversion == 'L_to_ml':
            scaled = scaled * 1000.0
        elif unit_conversion == 'ml_to_L':
            scaled = scaled / 1000.0
        elif unit_conversion == 'L_to_gal':
            scaled = scaled * 0.264172
        elif unit_conversion == 'gal_to_L':
            scaled = scaled / 0.264172
        else:
            raise ValueError("Unsupported unit conversion")
    return scaled

if __name__ == '__main__':
    sample_volumes = [1.5, 2.0, 3.7, 0.5, 4.2, 1.1, 5.0, 2.8, 3.3, 6.1]
    scaled_result = scale_volumes(sample_volumes, factor=2.5, unit_conversion='L_to_ml')
    print(scaled_result)
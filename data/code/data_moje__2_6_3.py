import numpy as np

def scale_volumes(volumes, scale_factor):
    volumes_array = np.array(volumes, dtype=np.float64)
    scaled_volumes = volumes_array * scale_factor
    return scaled_volumes

if __name__ == '__main__':
    sample_volumes = [10.5, 20.0, 35.75, 42.25, 50.0]
    factor = 2.5
    result = scale_volumes(sample_volumes, factor)
    print(result)
import numpy as np

def scale_volumes(volumes, scale_factor=2.0):
    volumes_array = np.asarray(volumes, dtype=np.float64)
    scaled_volumes = volumes_array * scale_factor
    return scaled_volumes
if __name__ == '__main__':
    sample_volumes = [1.5, 2.0, 3.7, 4.2, 5.8, 6.1, 7.3, 8.9, 9.0, 10.5]
    result = scale_volumes(sample_volumes)
    print(result)
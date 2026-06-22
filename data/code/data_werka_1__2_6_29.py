import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([10.5, 20.3, 30.7, 40.2, 50.9])
    scaling_factor = 1.5
    scaled_volumes = scale_volumes(sample_volumes, scaling_factor)
    print(scaled_volumes)
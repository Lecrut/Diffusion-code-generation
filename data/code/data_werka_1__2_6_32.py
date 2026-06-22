import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([10.0, 20.5, 30.75, 40.25])
    scaling_factor = 1.1
    scaled_volumes = scale_volumes(sample_volumes, scaling_factor)
    print(scaled_volumes)
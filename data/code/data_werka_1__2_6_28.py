import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    scaling_factor = 2.5
    scaled_volumes = scale_volumes(sample_volumes, scaling_factor)
    print(scaled_volumes)
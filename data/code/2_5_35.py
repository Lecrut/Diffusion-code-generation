import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([100, 200, 300, 400, 500])
    scaling_factor = 1.1
    scaled_volumes = scale_volumes(sample_volumes, scaling_factor)
    print(scaled_volumes)
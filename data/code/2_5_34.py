import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor
if __name__ == '__main__':
    sample_volumes = np.array([10.0, 20.5, 30.75, 40.0, 50.25])
    scale_factor = 1.5
    scaled_volumes = scale_volumes(sample_volumes, scale_factor)
    print(scaled_volumes)
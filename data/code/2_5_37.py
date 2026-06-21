import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([100.0, 200.0, 300.0, 400.0, 500.0])
    scale_factor = 1.1
    scaled_volumes = scale_volumes(sample_volumes, scale_factor)
    print(scaled_volumes)
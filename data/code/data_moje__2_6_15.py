import numpy as np

def scale_volumes(volumes, scale_factor):
    if not isinstance(volumes, np.ndarray):
        volumes = np.array(volumes, dtype=np.float64)
    return volumes * scale_factor

if __name__ == '__main__':
    sample_volumes = np.array([10.5, 20.0, 35.25, 50.0, 100.0])
    factor = 1.5
    result = scale_volumes(sample_volumes, factor)
    print(result)
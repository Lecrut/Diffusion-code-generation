import numpy as np

def scale_volumes(volumes, scale_factor):
    if not isinstance(volumes, np.ndarray):
        volumes = np.array(volumes, dtype=np.float64)
    return volumes * scale_factor

if __name__ == '__main__':
    sample_volumes = np.array([10.5, 20.0, 15.75, 30.25, 5.0])
    factor = 2.5
    result = scale_volumes(sample_volumes, factor)
    print(result)
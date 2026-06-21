import numpy as np

def validate_volumes(volumes):
    if not isinstance(volumes, np.ndarray):
        raise ValueError("Volumes must be provided as a NumPy array.")
    if volumes.ndim != 1:
        raise ValueError("Volumes must be a one-dimensional array.")

def validate_factor(factor):
    if not isinstance(factor, (int, float)):
        raise ValueError("Scaling factor must be an integer or a float.")
    if factor <= 0:
        raise ValueError("Scaling factor must be greater than zero.")

def scale_volumes(volumes, factor):
    validate_volumes(volumes)
    validate_factor(factor)
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([15.0, 25.5, 36.75, 48.0, 59.25])
    scaling_factor = 1.4
    scaled_volumes = scale_volumes(sample_volumes, scaling_factor)
    print(scaled_volumes)
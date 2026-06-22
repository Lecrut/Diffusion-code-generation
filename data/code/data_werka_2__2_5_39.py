import numpy as np

def validate_volumes(volumes):
    if not isinstance(volumes, np.ndarray):
        raise ValueError("Volumes must be a NumPy array.")
    if volumes.ndim != 1:
        raise ValueError("Volumes must be a one-dimensional array.")
    if not np.issubdtype(volumes.dtype, np.number):
        raise ValueError("All elements in volumes must be numbers.")

def validate_factor(factor):
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be an integer or float.")
    if factor <= 0:
        raise ValueError("Factor must be greater than zero.")

def scale_volumes(volumes, factor):
    validate_volumes(volumes)
    validate_factor(factor)
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([15.0, 25.5, 36.75, 48.0, 59.25])
    scale_factor = 1.3
    scaled_volumes = scale_volumes(sample_volumes, scale_factor)
    print(scaled_volumes)
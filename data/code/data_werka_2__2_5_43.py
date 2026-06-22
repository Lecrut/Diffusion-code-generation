import numpy as np

def validate_volumes(volumes):
    if not isinstance(volumes, (list, np.ndarray)):
        raise ValueError("Volumes must be a list or a NumPy array.")
    if not all(isinstance(v, (int, float)) for v in volumes):
        raise ValueError("All volume measurements must be numbers.")

def validate_factor(factor):
    if not isinstance(factor, (int, float)):
        raise ValueError("Scaling factor must be a number.")
    if factor <= 0:
        raise ValueError("Scaling factor must be greater than zero.")

def scale_volumes(volumes, factor):
    validate_volumes(volumes)
    validate_factor(factor)
    return np.array(volumes) * factor

if __name__ == '__main__':
    sample_volumes = [15.0, 25.25, 35.5, 45.75, 56.0]
    scaling_factor = 1.3
    scaled_volumes = scale_volumes(sample_volumes, scaling_factor)
    print(scaled_volumes)
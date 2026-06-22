import numpy as np

def validate_input(volumes, factor):
    if not isinstance(volumes, (np.ndarray, list)):
        raise ValueError("Volumes must be a NumPy array or a list.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Scaling factor must be an integer or a float.")
    if len(volumes) == 0:
        raise ValueError("The volumes array cannot be empty.")

def scale_volumes(volumes, factor):
    validate_input(volumes, factor)
    return np.array(volumes) * factor

if __name__ == '__main__':
    sample_volumes = [5.0, 15.25, 25.5, 35.75, 46.0]
    scaling_factor = 1.2
    scaled_volumes = scale_volumes(sample_volumes, scaling_factor)
    print(scaled_volumes)
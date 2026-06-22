import numpy as np

def validate_input(volumes, factor):
    if not isinstance(volumes, np.ndarray):
        raise ValueError("Volumes must be a NumPy array.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be an integer or a float.")
    if volumes.ndim != 1:
        raise ValueError("Volumes array must be one-dimensional.")

def scale_volumes(volumes, factor):
    validate_input(volumes, factor)
    return volumes * factor

class VolumeScaler:
    def __init__(self, initial_volumes, scaling_factor):
        self.volumes = np.array(initial_volumes)
        self.scaling_factor = scaling_factor
        validate_input(self.volumes, self.scaling_factor)

    def apply_scale(self):
        return self.volumes * self.scaling_factor

if __name__ == '__main__':
    sample_volumes = np.array([5.0, 10.25, 15.5, 20.75, 26.0])
    scaling_factor = 1.3
    try:
        scaled_volumes_func = scale_volumes(sample_volumes, scaling_factor)
        print("Scaled volumes using function:", scaled_volumes_func)

        scaler = VolumeScaler(sample_volumes, scaling_factor)
        scaled_volumes_class = scaler.apply_scale()
        print("Scaled volumes using class:", scaled_volumes_class)
    except ValueError as e:
        print(e)
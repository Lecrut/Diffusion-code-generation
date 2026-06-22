import numpy as np

def validate_input(volumes, factor):
    if not isinstance(volumes, (list, np.ndarray)):
        raise ValueError("Volumes must be a list or NumPy array.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Factor must be an integer or float.")
    if len(volumes) == 0:
        raise ValueError("Volumes cannot be empty.")

def scale_volumes(volumes, factor):
    validate_input(volumes, factor)
    return np.array(volumes) * factor

class VolumeScaler:
    def __init__(self, initial_volumes, scaling_factor):
        self.volumes = np.array(initial_volumes)
        self.scaling_factor = scaling_factor
    
    def apply_scale(self):
        validate_input(self.volumes, self.scaling_factor)
        return self.volumes * self.scaling_factor

if __name__ == '__main__':
    sample_volumes = [10.5, 21.0, 31.5, 42.0, 52.5]
    scaling_factor = 1.3
    try:
        scaled_volumes_func = scale_volumes(sample_volumes, scaling_factor)
        print("Scaled volumes using function:", scaled_volumes_func)
        
        scaler = VolumeScaler(sample_volumes, scaling_factor)
        scaled_volumes_class = scaler.apply_scale()
        print("Scaled volumes using class:", scaled_volumes_class)
    except ValueError as e:
        print(e)
import numpy as np

def validate_input(volumes, factor):
    if not isinstance(volumes, np.ndarray) or not volumes.dtype.kind in 'fiu':
        raise ValueError("Volumes must be a NumPy array of numeric type.")
    if not isinstance(factor, (int, float)):
        raise ValueError("Scaling factor must be an integer or float.")

def scale_volumes(volumes, factor):
    validate_input(volumes, factor)
    return volumes * factor

class VolumeScaler:
    def __init__(self, initial_volumes, scaling_factor):
        self.volumes = np.array(initial_volumes)
        self.scaling_factor = scaling_factor
        validate_input(self.volumes, self.scaling_factor)
    
    def apply_scale(self):
        return scale_volumes(self.volumes, self.scaling_factor)

if __name__ == '__main__':
    sample_volumes = np.array([10.5, 20.75, 30.0, 40.25, 50.5])
    scaling_factor = 1.3
    scaled_volumes_direct = scale_volumes(sample_volumes, scaling_factor)
    print("Directly scaled volumes:", scaled_volumes_direct)

    scaler = VolumeScaler([5.0, 15.25, 25.5, 35.75, 46.0], 1.4)
    scaled_volumes_class = scaler.apply_scale()
    print("Scaled volumes using class:", scaled_volumes_class)
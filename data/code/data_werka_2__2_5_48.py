import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

class VolumeScaler:

    def __init__(self, initial_volumes, scaling_factor):
        self.volumes = np.array(initial_volumes)
        self.scaling_factor = scaling_factor

    def apply_scale(self):
        return self.volumes * self.scaling_factor

    def set_scaling_factor(self, new_factor):
        self.scaling_factor = new_factor
if __name__ == '__main__':
    sample_volumes = np.array([15.0, 25.5, 36.0, 46.5, 57.0])
    scaling_factor = 1.3
    scaler = VolumeScaler(sample_volumes, scaling_factor)
    scaled_volumes = scaler.apply_scale()
    print(scaled_volumes)
    new_scaling_factor = 1.4
    scaler.set_scaling_factor(new_scaling_factor)
    updated_scaled_volumes = scaler.apply_scale()
    print(updated_scaled_volumes)
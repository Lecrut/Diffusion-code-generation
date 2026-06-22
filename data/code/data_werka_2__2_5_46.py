import numpy as np

class VolumeScaler:

    def __init__(self, initial_volumes):
        self.volumes = np.array(initial_volumes)

    def set_scaling_factor(self, factor):
        if factor <= 0:
            raise ValueError('Scaling factor must be positive')
        self.scaling_factor = factor

    def apply_scale(self):
        return self.volumes * self.scaling_factor
if __name__ == '__main__':
    initial_volumes = [1.0, 2.5, 4.0, 6.5, 9.0]
    scaler = VolumeScaler(initial_volumes)
    scaler.set_scaling_factor(2.0)
    scaled_volumes = scaler.apply_scale()
    print('Scaled Volumes:', scaled_volumes)
    scaler.set_scaling_factor(1.5)
    another_scaled_volumes = scaler.apply_scale()
    print('Another Scaled Volumes:', another_scaled_volumes)
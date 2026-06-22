import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

class VolumeScaler:
    def __init__(self, initial_volumes, scaling_factor):
        self.volumes = np.array(initial_volumes)
        self.scaling_factor = scaling_factor

    def apply_scale(self):
        return self.volumes * self.scaling_factor

if __name__ == '__main__':
    initial_volumes = [5.0, 15.25, 25.5, 35.75, 46.0]
    scaling_factor = 1.2
    scaler = VolumeScaler(initial_volumes, scaling_factor)
    scaled_volumes = scaler.apply_scale()
    print(scaled_volumes)
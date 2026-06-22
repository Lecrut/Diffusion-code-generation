import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

class VolumeProcessor:
    def __init__(self, initial_volumes):
        self.volumes = np.array(initial_volumes)
    
    def set_scaling_factor(self, factor):
        if factor <= 0:
            raise ValueError("Scaling factor must be greater than zero")
        self.scaling_factor = factor
    
    def apply_scale(self):
        return scale_volumes(self.volumes, self.scaling_factor)

if __name__ == '__main__':
    initial_volumes = [7.5, 17.75, 27.0, 36.25, 45.5]
    processor = VolumeProcessor(initial_volumes)
    processor.set_scaling_factor(1.3)
    scaled_volumes = processor.apply_scale()
    print(scaled_volumes)
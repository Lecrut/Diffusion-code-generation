import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

class VolumeProcessor:
    def __init__(self, initial_volumes, scaling_factor):
        self.volumes = np.array(initial_volumes)
        self.scaling_factor = scaling_factor
    
    def apply_scale(self):
        return scale_volumes(self.volumes, self.scaling_factor)

if __name__ == '__main__':
    sample_volumes = [2.0, 4.5, 6.75, 8.0, 10.25]
    scaling_factor = 1.3
    processor = VolumeProcessor(sample_volumes, scaling_factor)
    scaled_volumes = processor.apply_scale()
    print(scaled_volumes)
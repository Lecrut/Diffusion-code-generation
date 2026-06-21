import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

class VolumeProcessor:
    def __init__(self, initial_volumes):
        self.volumes = np.array(initial_volumes)
    
    def set_scaling_factor(self, factor):
        self.scaling_factor = factor
    
    def apply_scale(self):
        if not hasattr(self, 'scaling_factor'):
            raise ValueError("Scaling factor has not been set.")
        return self.volumes * self.scaling_factor

if __name__ == '__main__':
    sample_volumes = np.array([50.0, 75.25, 100.5, 125.75, 150.0])
    scaling_factors = {'factor1': 1.3, 'factor2': 1.4, 'factor3': 1.5}
    
    processor = VolumeProcessor(sample_volumes)
    processor.set_scaling_factor(scaling_factors['factor2'])
    scaled_volumes = processor.apply_scale()
    print(scaled_volumes)
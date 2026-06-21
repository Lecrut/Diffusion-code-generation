import numpy as np

class VolumeProcessor:
    def __init__(self, volumes):
        self.volumes = np.array(volumes)
    
    def scale(self, factor):
        return self.volumes * factor
    
    def add_constant(self, constant):
        return self.volumes + constant

if __name__ == '__main__':
    sample_volumes = [50.0, 100.5, 150.75, 200.0, 250.25]
    volume_processor = VolumeProcessor(sample_volumes)
    
    scale_factor = 1.3
    scaled_volumes = volume_processor.scale(scale_factor)
    print("Scaled Volumes:", scaled_volumes)
    
    constant_addition = 5.0
    added_volumes = volume_processor.add_constant(constant_addition)
    print("Added Constant to Volumes:", added_volumes)
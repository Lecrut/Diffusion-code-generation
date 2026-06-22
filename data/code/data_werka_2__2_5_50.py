import numpy as np

class VolumeProcessor:
    def __init__(self, volumes):
        self.volumes = np.array(volumes)

    def scale(self, factor):
        return self.volumes * factor

    def add_offset(self, offset):
        return self.volumes + offset

if __name__ == '__main__':
    sample_volumes = [1.0, 2.5, 3.75, 4.0, 5.25]
    processor = VolumeProcessor(sample_volumes)
    
    scale_factor = 2.0
    scaled_volumes = processor.scale(scale_factor)
    print("Scaled Volumes:", scaled_volumes)
    
    offset_value = 1.0
    offset_volumes = processor.add_offset(offset_value)
    print("Offset Volumes:", offset_volumes)
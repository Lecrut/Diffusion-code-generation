import numpy as np

class VolumeProcessor:
    def __init__(self, volumes):
        self.volumes = np.array(volumes)

    def scale(self, factor):
        return self.volumes * factor

    def average_volume(self):
        return np.mean(self.volumes)

if __name__ == '__main__':
    sample_volumes = [15.0, 25.5, 36.0, 46.5, 57.0]
    processor = VolumeProcessor(sample_volumes)
    
    scale_factor = 1.3
    scaled_volumes = processor.scale(scale_factor)
    print("Scaled Volumes:", scaled_volumes)
    
    average_volume = processor.average_volume()
    print("Average Volume:", average_volume)
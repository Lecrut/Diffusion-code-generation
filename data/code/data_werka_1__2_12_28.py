import numpy as np

class VolumeData:
    def __init__(self, data):
        self.data = np.array(data, dtype=np.float32)

    def scale(self, factor):
        self.data *= factor

    def get_data(self):
        return self.data

if __name__ == '__main__':
    sample_data = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ]
    
    volume = VolumeData(sample_data)
    scale_factor = 2.5
    volume.scale(scale_factor)
    print(volume.get_data())
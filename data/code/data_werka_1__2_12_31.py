import numpy as np

class VolumeDataStore:
    def __init__(self, data):
        self.data = np.array(data, dtype=np.float32)
    
    def scale_volumes(self, factor):
        self.data *= factor
    
    def get_data(self):
        return self.data.tolist()

if __name__ == '__main__':
    sample_data = [1.0, 2.5, 3.75, 4.0]
    store = VolumeDataStore(sample_data)
    
    print("Original Data:", store.get_data())
    
    scale_factor = 2.0
    store.scale_volumes(scale_factor)
    
    print("Scaled Data:", store.get_data())
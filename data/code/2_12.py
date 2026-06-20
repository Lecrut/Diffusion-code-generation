import struct
import math

class EfficientVolumeData:
    def __init__(self):
        self.base_volumes = []
        self.base_scales = []
        self.current_scale_factor = 1.0

    def add_volume(self, volume, scale_reference=1.0):
        self.base_volumes.append(volume)
        self.base_scales.append(scale_reference)

    def set_scale_factor(self, factor):
        self.current_scale_factor = factor

    def get_volume(self, index):
        if index < 0 or index >= len(self.base_volumes):
            raise IndexError("Volume index out of range")
        return self.base_volumes[index] * (self.current_scale_factor ** 3) / (self.base_scales[index] ** 3)

    def get_all_volumes(self):
        results = []
        for i in range(len(self.base_volumes)):
            results.append(self.get_volume(i))
        return results

    def memory_usage(self):
        return len(self.base_volumes) * 8 + len(self.base_scales) * 8

def create_sample_data():
    data_store = EfficientVolumeData()
    data_store.add_volume(100.0)
    data_store.add_volume(200.0)
    data_store.add_volume(350.5)
    
    data_store.set_scale_factor(2.0)
    
    vol1 = data_store.get_volume(0)
    vol2 = data_store.get_volume(1)
    all_vols = data_store.get_all_volumes()
    
    return vol1, vol2, all_vols

if __name__ == '__main__':
    v1, v2, all_v = create_sample_data()
    print(v1)
    print(v2)
    print(all_v)
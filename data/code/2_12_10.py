import array
import math

SCALE_CUBIC = 3.0
BASE_SCALE = 1.0

class CompactVolumeManager:
    def __init__(self):
        self._raw_volumes = array.array('d')
        self._reference_scales = array.array('d')
        self._global_scale = BASE_SCALE

    def insert_measurement(self, volume_value, reference_scale=BASE_SCALE):
        self._raw_volumes.append(volume_value)
        self._reference_scales.append(reference_scale)

    def update_global_scale(self, new_scale):
        self._global_scale = float(new_scale)

    def retrieve_volume(self, index):
        count = len(self._raw_volumes)
        if index < 0 or index >= count:
            raise IndexError("Index out of bounds for volume data")
        base_vol = self._raw_volumes[index]
        ref_scale = self._reference_scales[index]
        scale_ratio = self._global_scale / ref_scale
        return base_vol * (scale_ratio ** SCALE_CUBIC)

    def retrieve_all_scaled(self):
        results = []
        count = len(self._raw_volumes)
        for i in range(count):
            results.append(self.retrieve_volume(i))
        return results

    def get_total_volume(self):
        total = 0.0
        count = len(self._raw_volumes)
        for i in range(count):
            total += self.retrieve_volume(i)
        return total

if __name__ == '__main__':
    manager = CompactVolumeManager()
    manager.insert_measurement(100.0, 1.0)
    manager.insert_measurement(200.0, 2.0)
    manager.insert_measurement(50.0, 0.5)
    
    manager.update_global_scale(2.0)
    
    single_val = manager.retrieve_volume(1)
    all_vals = manager.retrieve_all_scaled()
    total_vol = manager.get_total_volume()
    
    print(single_val)
    print(all_vals)
    print(total_vol)
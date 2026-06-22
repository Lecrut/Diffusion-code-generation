import array
import math

class VolumeDataStore:
    def __init__(self):
        self._data = array.array('d')
        self._scale_factor = 1.0

    def add_volume(self, x, y, z):
        base_volume = x * y * z
        self._data.append(base_volume)

    def set_scale(self, factor):
        self._scale_factor = factor

    def get_volume(self, index):
        if 0 <= index < len(self._data):
            return self._data[index] * self._scale_factor
        raise IndexError("Volume index out of range")

    def get_total_volume(self):
        return sum(self._data) * self._scale_factor

    def get_count(self):
        return len(self._data)

    def get_all_scaled_volumes(self):
        return [v * self._scale_factor for v in self._data]

if __name__ == '__main__':
    store = VolumeDataStore()
    store.add_volume(2.0, 3.0, 4.0)
    store.add_volume(1.0, 1.0, 1.0)
    store.add_volume(5.0, 2.0, 2.0)
    
    print(store.get_volume(0))
    print(store.get_volume(1))
    print(store.get_volume(2))
    print(store.get_total_volume())
    
    store.set_scale(2.0)
    print(store.get_volume(0))
    print(store.get_total_volume())
    print(store.get_all_scaled_volumes())
import math
import struct

class VolumeStore:
    def __init__(self):
        self._data = {}

    def set(self, key, value):
        if not isinstance(key, tuple):
            raise TypeError("Key must be a tuple of coordinates.")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric.")
        self._data[key] = float(value)

    def get(self, key):
        if not isinstance(key, tuple):
            raise TypeError("Key must be a tuple of coordinates.")
        return self._data.get(key, 0.0)

    def scale(self, factor):
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be numeric.")
        if factor == 0:
            self._data.clear()
            return
        
        new_data = {}
        for key, value in self._data.items():
            new_key = tuple(math.floor(coord * factor) for coord in key)
            new_data[new_key] = value
        
        self._data = new_data

    def get_total_volume(self):
        return sum(self._data.values())

    def get_max_key(self):
        if not self._data:
            return None
        return max(self._data.keys())

    def get_min_key(self):
        if not self.data:
            return None
        return min(self._data.keys())

if __name__ == '__main__':
    store = VolumeStore()
    
    store.set((1, 2, 3), 10.0)
    store.set((4, 5, 6), 20.0)
    store.set((2, 2, 2), 5.0)
    
    total = store.get_total_volume()
    print(total)
    
    max_key = store.get_max_key()
    print(max_key)
    
    scale_factor = 2
    store.scale(scale_factor)
    
    new_val = store.get((2, 4, 6))
    print(new_val)
    
    new_total = store.get_total_volume()
    print(new_total)
    
    new_max_key = store.get_max_key()
    print(new_max_key)
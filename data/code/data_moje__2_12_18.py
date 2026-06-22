import numpy as np

class EfficientVolumeStore:
    def __init__(self):
        self._data = {}
        self._scales = {}

    def add_volume(self, identifier, shape, factor=1.0):
        data = np.zeros(shape, dtype=np.float64)
        self._data[identifier] = data
        self._scales[identifier] = factor

    def set_volume_data(self, identifier, array):
        if identifier not in self._data:
            raise KeyError("Identifier not found")
        self._data[identifier][:] = array

    def get_volume(self, identifier, scale_factor=1.0):
        if identifier not in self._data:
            raise KeyError("Identifier not found")
        base_scale = self._scales[identifier]
        total_scale = base_scale * scale_factor
        return self._data[identifier] * total_scale

    def update_scale(self, identifier, new_factor):
        if identifier not in self._scales:
            raise KeyError("Identifier not found")
        self._scales[identifier] = new_factor

    def remove_volume(self, identifier):
        if identifier in self._data:
            del self._data[identifier]
            del self._scales[identifier]

    def list_identifiers(self):
        return list(self._data.keys())

if __name__ == '__main__':
    store = EfficientVolumeStore()

    store.add_volume("cube1", (10, 10, 10), factor=2.0)
    store.add_volume("sphere1", (5, 5, 5), factor=0.5)

    cube_data = np.ones((10, 10, 10)) * 3.0
    store.set_volume_data("cube1", cube_data)

    sphere_data = np.ones((5, 5, 5)) * 4.0
    store.set_volume_data("sphere1", sphere_data)

    result_cube = store.get_volume("cube1")
    print(result_cube[0, 0, 0])

    result_sphere = store.get_volume("sphere1", scale_factor=2.0)
    print(result_sphere[0, 0, 0])

    store.update_scale("cube1", 5.0)
    result_cube_updated = store.get_volume("cube1")
    print(result_cube_updated[0, 0, 0])

    print(store.list_identifiers())

    store.remove_volume("sphere1")
    print(store.list_identifiers())
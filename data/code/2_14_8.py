import math
class ScalableVolumeStore:
    def __init__(self, base_data):
        self.base_data = base_data
        self.scale_factor = 1.0
        self.scaled_data = self._scale_data(base_data)
    def _scale_data(self, data):
        return [item * self.scale_factor for item in data]
    def set_scale_factor(self, factor):
        self.scale_factor = float(factor)
        self.scaled_data = self._scale_data(self.base_data)
    def get_volume(self, index):
        if 0 <= index < len(self.scaled_data):
            return self.scaled_data[index]
        raise IndexError("Index out of bounds")
    def get_base_data(self):
        return self.base_data
if __name__ == '__main__':
    sample_volumes = [10.0, 20.5, 33.1, 45.9]
    initial_scale = 2.5
    store = ScalableVolumeStore(sample_volumes)
    store.set_scale_factor(initial_scale)
    print(f"Base Data: {store.get_base_data()}")
    print(f"Scale Factor: {store.scale_factor}")
    index_to_retrieve = 1
    retrieved_volume = store.get_volume(index_to_retrieve)
    print(f"Volume at index {index_to_retrieve}: {retrieved_volume}")
    new_scale = 1.5
    store.set_scale_factor(new_scale)
    print(f"\nNew Scale Factor: {store.scale_factor}")
    retrieved_volume_new = store.get_volume(index_to_retrieve)
    print(f"Volume at index {index_to_retrieve} with new scale: {retrieved_volume_new}")
    index_to_retrieve = 3
    retrieved_volume_final = store.get_volume(index_to_retrieve)
    print(f"Volume at index {index_to_retrieve} with new scale: {retrieved_volume_final}")
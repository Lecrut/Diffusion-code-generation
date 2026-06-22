import array

class VolumeStore:
    def __init__(self):
        self._data = array.array('d', [])
        self._scale = 1.0

    def store(self, values):
        for val in values:
            self._data.append(val)

    def get_all_scaled(self, scale_factor):
        if not self._data:
            return []
        scaled_values = array.array('d', [v * scale_factor for v in self._data])
        return list(scaled_values)

    def retrieve_at(self, index):
        if 0 <= index < len(self._data):
            return self._data[index] * self._scale
        return None

    def resize_scale(self, new_scale):
        self._scale = new_scale

if __name__ == '__main__':
    store = VolumeStore()
    initial_values = [10.5, 20.0, 30.25, 40.75]
    store.store(initial_values)
    store.resize_scale(2.0)
    result_scaled = store.get_all_scaled(1.5)
    specific_value = store.retrieve_at(2)
    print(f"Scaled List: {result_scaled}")
    print(f"Specific Value: {specific_value}")
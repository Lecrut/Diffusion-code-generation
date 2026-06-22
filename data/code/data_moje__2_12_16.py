class VolumeDataStore:
    def __init__(self):
        self._data = []
        self._scale = 1.0

    def add_volume(self, value):
        self._data.append(value)

    def set_scale(self, factor):
        self._scale = factor

    def get_total_scaled_volume(self):
        return sum(self._data) * self._scale

    def get_individual_scaled_volumes(self):
        return [v * self._scale for v in self._data]

    def clear(self):
        self._data.clear()
        self._scale = 1.0

if __name__ == '__main__':
    store = VolumeDataStore()
    store.add_volume(10)
    store.add_volume(20)
    store.add_volume(30)
    store.set_scale(1.5)
    total = store.get_total_scaled_volume()
    individual = store.get_individual_scaled_volumes()
    print(total)
    print(individual)
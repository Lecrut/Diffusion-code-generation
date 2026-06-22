class VolumeStore:
    def __init__(self):
        self._base_volumes = {}
        self._scale_factor = 1.0

    def store_volume(self, key, value):
        self._base_volumes[key] = value

    def set_scale_factor(self, factor):
        self._scale_factor = float(factor)

    def get_volume(self, key):
        if key not in self._base_volumes:
            return 0.0
        return self._base_volumes[key] * self._scale_factor

    def get_all_scaled_volumes(self):
        return {key: value * self._scale_factor for key, value in self._base_volumes.items()}

if __name__ == '__main__':
    store = VolumeStore()
    store.store_volume('tank_a', 100)
    store.store_volume('tank_b', 250)
    store.set_scale_factor(2.5)
    print(store.get_volume('tank_a'))
    print(store.get_volume('tank_b'))
    print(store.get_all_scaled_volumes())
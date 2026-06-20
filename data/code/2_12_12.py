class VolumeStore:
    def __init__(self, base_unit_factor=1.0):
        self._base_factor = float(base_unit_factor)
        self._volume = 0.0

    def add_measurement(self, value, unit_factor=1.0):
        adjusted_value = value * unit_factor
        self._volume += adjusted_value

    def get_current_volume(self, scale_factor=1.0):
        if scale_factor == 0:
            return 0.0
        return self._volume * self._base_factor * scale_factor

    def set_base_unit(self, factor):
        self._base_factor = float(factor)

    def reset(self):
        self._volume = 0.0

if __name__ == '__main__':
    store = VolumeStore(base_unit_factor=1.5)
    store.add_measurement(10, unit_factor=2.0)
    store.add_measurement(5, unit_factor=3.0)
    result_unscaled = store.get_current_volume(scale_factor=1.0)
    result_scaled = store.get_current_volume(scale_factor=2.0)
    print(result_unscaled)
    print(result_scaled)
    store.set_base_unit(0.5)
    print(store.get_current_volume(scale_factor=1.0))
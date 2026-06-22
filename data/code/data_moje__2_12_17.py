class VolumeScaleStore:
    def __init__(self, base_volumes):
        self._base_volumes = list(base_volumes)
        self._scale_factor = 1.0

    def set_scale_factor(self, factor):
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self._scale_factor = float(factor)

    def get_volume(self, index):
        if index < 0 or index >= len(self._base_volumes):
            raise IndexError("Volume index out of range")
        return self._base_volumes[index] * self._scale_factor

    def get_volumes_range(self, start, end):
        if start < 0 or end > len(self._base_volumes) or start > end:
            raise IndexError("Range indices out of bounds")
        return [v * self._scale_factor for v in self._base_volumes[start:end]]

    def add_volume(self, value):
        self._base_volumes.append(float(value))

    def base_volumes(self):
        return list(self._base_volumes)

    def current_scale(self):
        return self._scale_factor

if __name__ == '__main__':
    initial_data = [10.5, 20.0, 35.5, 50.0]
    store = VolumeScaleStore(initial_data)
    print(store.get_volume(0))
    store.set_scale_factor(2.0)
    print(store.get_volume(1))
    print(store.get_volumes_range(0, 2))
    store.add_volume(60.0)
    print(store.get_volume(3))
    print(store.current_scale())
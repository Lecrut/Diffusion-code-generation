class VolumeStore:
    def __init__(self):
        self._base_value = 0.0
        self._scale_factor = 1.0

    def store(self, value):
        self._base_value = float(value)
        self._scale_factor = 1.0

    def retrieve(self):
        return self._base_value * self._scale_factor

    def scale(self, factor):
        self._scale_factor = self._scale_factor * float(factor)

    def reset_scale(self):
        self._scale_factor = 1.0

if __name__ == '__main__':
    store = VolumeStore()
    store.store(100.0)
    print(store.retrieve())
    store.scale(2.5)
    print(store.retrieve())
    store.scale(0.4)
    print(store.retrieve())
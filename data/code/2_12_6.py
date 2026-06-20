class ScaledVolumeStore:
    def __init__(self, base_volume: float, scale_factor: float = 1.0):
        self._base_volume = base_volume
        self._scale_factor = scale_factor

    def set_base_volume(self, value: float) -> None:
        self._base_volume = value

    def set_scale_factor(self, value: float) -> None:
        self._scale_factor = value

    def get_retrieved_volume(self) -> float:
        return self._base_volume * self._scale_factor

    def get_base_volume(self) -> float:
        return self._base_volume

    def get_scale_factor(self) -> float:
        return self._scale_factor

if __name__ == '__main__':
    initial_base = 500.0
    initial_scale = 2.5
    store = ScaledVolumeStore(initial_base, initial_scale)
    
    print(store.get_retrieved_volume())
    
    new_base = 1000.0
    new_scale = 0.5
    store.set_base_volume(new_base)
    store.set_scale_factor(new_scale)
    
    print(store.get_retrieved_volume())
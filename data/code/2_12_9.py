class VolumeStore:
    def __init__(self):
        self._base_volumes = {}
        self._scaling_factors = []
        self._factor_map = {}

    def add_volume(self, name, value):
        if name in self._base_volumes:
            raise ValueError(f"Volume '{name}' already exists.")
        self._base_volumes[name] = value

    def set_scale_factor(self, name, factor):
        if name not in self._base_volumes:
            raise ValueError(f"Volume '{name}' does not exist.")
        self._factor_map[name] = factor
        if factor not in self._scaling_factors:
            self._scaling_factors.append(factor)

    def get_scaled_volume(self, name):
        if name not in self._base_volumes:
            raise KeyError(f"Volume '{name}' not found.")
        base = self._base_volumes[name]
        factor = self._factor_map.get(name, 1.0)
        return base * factor

    def get_all_scaled(self):
        result = {}
        for name in self._base_volumes:
            result[name] = self.get_scaled_volume(name)
        return result

if __name__ == '__main__':
    store = VolumeStore()
    store.add_volume("water", 100.0)
    store.add_volume("oil", 50.0)
    store.set_scale_factor("water", 2.5)
    store.set_scale_factor("oil", 1.0)
    
    water_volume = store.get_scaled_volume("water")
    print(water_volume)
    
    all_volumes = store.get_all_scaled()
    print(all_volumes)
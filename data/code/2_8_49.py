class VolumeStore:
    def __init__(self):
        self.volumes = {}

    def add_volume(self, key, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError('Volume must be a number')
        self.volumes[key] = volume

    def get_volume(self, key):
        return self.volumes.get(key, None)

    def scale_volumes(self, factor):
        for key in self.volumes:
            self.volumes[key] *= factor

if __name__ == '__main__':
    store = VolumeStore()
    store.add_volume('cylinder', 314.16)
    store.add_volume('cone', 157.08)

    print("Original volumes:")
    print(f"Cylinder: {store.get_volume('cylinder')}")
    print(f"Cone: {store.get_volume('cone')}")

    scale_factor = 1.5
    store.scale_volumes(scale_factor)

    print("\nScaled volumes by factor of 1.5:")
    print(f"Cylinder: {store.get_volume('cylinder')}")
    print(f"Cone: {store.get_volume('cone')}")
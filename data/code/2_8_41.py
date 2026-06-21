class VolumeStore:
    def __init__(self):
        self.volumes = {}

    def add_volume(self, key, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number")
        self.volumes[key] = volume

    def get_volume(self, key):
        return self.volumes.get(key, None)

    def scale_volumes(self, factor):
        for key in self.volumes:
            self.volumes[key] *= factor

if __name__ == '__main__':
    store = VolumeStore()
    store.add_volume('tank', 1000)
    store.add_volume('pond', 500)

    print("Original volumes:")
    print(store.get_volume('tank'))

    store.scale_volumes(1.5)
    print("Scaled volumes:")
    print(store.get_volume('tank'))
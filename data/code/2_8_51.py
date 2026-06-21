class VolumeData:

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
    CUBE_VOLUME = 27.0
    SPHERE_VOLUME = 52.36
    SCALE_FACTOR = 1.5
    volume_data = VolumeData()
    volume_data.add_volume('cube', CUBE_VOLUME)
    volume_data.add_volume('sphere', SPHERE_VOLUME)
    print('Original volumes:')
    print(f"Cube: {volume_data.get_volume('cube')}")
    print(f"Sphere: {volume_data.get_volume('sphere')}")
    volume_data.scale_volumes(SCALE_FACTOR)
    print('\nScaled volumes:')
    print(f"Cube: {volume_data.get_volume('cube')}")
    print(f"Sphere: {volume_data.get_volume('sphere')}")
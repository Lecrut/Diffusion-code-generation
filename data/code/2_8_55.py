class VolumeManager:
    DEFAULT_FACTOR = 1.0

    def __init__(self):
        self.volumes = {}

    def add_volume(self, key, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError('Volume must be a number')
        self.volumes[key] = volume

    def get_volume(self, key):
        return self.volumes.get(key, None)

    def scale_volumes(self, factor=DEFAULT_FACTOR):
        for key in self.volumes:
            self.volumes[key] *= factor

    @staticmethod
    def validate_factor(factor):
        if not isinstance(factor, (int, float)) or factor <= 0:
            raise ValueError('Factor must be a positive number')

if __name__ == '__main__':
    manager = VolumeManager()
    manager.add_volume('tank', 1000)
    manager.add_volume('pool', 5000)

    print('Original volumes:')
    print(f"Tank: {manager.get_volume('tank')}")
    print(f"Pool: {manager.get_volume('pool')}")

    scale_factor = 1.5
    VolumeManager.validate_factor(scale_factor)
    manager.scale_volumes(scale_factor)

    print('\nScaled volumes:')
    print(f"Tank: {manager.get_volume('tank')}")
    print(f"Pool: {manager.get_volume('pool')}")
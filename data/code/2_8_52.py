class VolumeData:

    def __init__(self):
        self.data = {}

    def add_volume(self, key, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError('Volume must be a number')
        self.data[key] = volume

    def get_volume(self, key):
        return self.data.get(key, None)

    def scale_volumes(self, factor):
        for key in self.data:
            self.data[key] *= factor
if __name__ == '__main__':
    volume_manager = VolumeData()
    volume_manager.add_volume('tank', 500)
    volume_manager.add_volume('reservoir', 1200)
    print('Original volumes:')
    for key in ['tank', 'reservoir']:
        print(f'{key}: {volume_manager.get_volume(key)}')
    scale_factor = 1.5
    volume_manager.scale_volumes(scale_factor)
    print('\nScaled volumes:')
    for key in ['tank', 'reservoir']:
        print(f'{key}: {volume_manager.get_volume(key)}')
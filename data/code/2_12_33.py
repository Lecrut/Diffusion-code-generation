class VolumeData:

    def __init__(self):
        self.data = {}

    def add_volume(self, key, volume):
        self.data[key] = volume

    def get_volume(self, key):
        return self.data.get(key, None)

    def scale_volumes(self, factor):
        for key in self.data:
            self.data[key] *= factor
if __name__ == '__main__':
    sample_data = {'cube': 27, 'sphere': 52.36, 'cylinder': 199.44}
    volume_manager = VolumeData()
    for key, value in sample_data.items():
        volume_manager.add_volume(key, value)
    print('Original volumes:')
    for key in sample_data:
        print(f'{key}: {volume_manager.get_volume(key)}')
    scale_factor = 2.0
    volume_manager.scale_volumes(scale_factor)
    print('\nScaled volumes:')
    for key in sample_data:
        print(f'{key}: {volume_manager.get_volume(key)}')
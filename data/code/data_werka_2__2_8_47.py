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
    vd = VolumeData()
    vd.add_volume('cube', 27)
    vd.add_volume('sphere', 52.36)
    print('Original volumes:')
    print(vd.get_volume('cube'))
    print(vd.get_volume('sphere'))
    vd.scale_volumes(2)
    print('\nScaled volumes by factor of 2:')
    print(vd.get_volume('cube'))
    print(vd.get_volume('sphere'))
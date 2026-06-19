class VolumeData:

    def __init__(self):
        self.data = {}

    def add_volume(self, key, volume):
        if key in self.data:
            raise ValueError('Key already exists')
        self.data[key] = volume

    def get_volume(self, key):
        return self.data.get(key, None)

    def scale_volumes(self, factor):
        for key in self.data:
            self.data[key] *= factor
if __name__ == '__main__':
    volumes = VolumeData()
    volumes.add_volume('cube', 27)
    volumes.add_volume('sphere', 113.097)
    print('Original cube volume:', volumes.get_volume('cube'))
    print('Original sphere volume:', volumes.get_volume('sphere'))
    volumes.scale_volumes(2)
    print('Scaled cube volume:', volumes.get_volume('cube'))
    print('Scaled sphere volume:', volumes.get_volume('sphere'))
class VolumeData:

    def __init__(self):
        self.data = {}

    def add_volume(self, key, volume):
        self.data[key] = volume

    def scale_volumes(self, factor):
        for key in self.data:
            self.data[key] *= factor

    def get_volume(self, key):
        return self.data.get(key, None)
if __name__ == '__main__':
    volumes = VolumeData()
    volumes.add_volume('room1', 50)
    volumes.add_volume('room2', 75)
    volumes.add_volume('room3', 100)
    volumes.scale_volumes(2)
    print(volumes.get_volume('room1'))
    print(volumes.get_volume('room2'))
    print(volumes.get_volume('room3'))
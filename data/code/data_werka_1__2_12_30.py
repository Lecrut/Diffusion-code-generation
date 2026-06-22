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
    volume_data = VolumeData()
    volume_data.add_volume('room1', 50)
    volume_data.add_volume('room2', 75)
    print('Original volumes:')
    print(f"Room 1: {volume_data.get_volume('room1')}")
    print(f"Room 2: {volume_data.get_volume('room2')}")
    volume_data.scale_volumes(2)
    print('\nScaled volumes:')
    print(f"Room 1: {volume_data.get_volume('room1')}")
    print(f"Room 2: {volume_data.get_volume('room2')}")
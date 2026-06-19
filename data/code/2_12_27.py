class VolumeData:
    def __init__(self):
        self.data = {}

    def add_volume(self, key, value):
        self.data[key] = value

    def get_volume(self, key):
        return self.data.get(key, 0)

    def scale_volumes(self, factor):
        for key in self.data:
            self.data[key] *= factor

if __name__ == '__main__':
    volume_data = VolumeData()
    volume_data.add_volume('room1', 100)
    volume_data.add_volume('room2', 200)
    print("Volume of room1:", volume_data.get_volume('room1'))
    print("Volume of room2:", volume_data.get_volume('room2'))
    
    scale_factor = 1.5
    volume_data.scale_volumes(scale_factor)
    print("Scaled Volume of room1:", volume_data.get_volume('room1'))
    print("Scaled Volume of room2:", volume_data.get_volume('room2'))
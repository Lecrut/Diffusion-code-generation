class VolumeData:
    def __init__(self):
        self.data = {}

    def add_volume(self, key, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number")
        self.data[key] = volume

    def scale_volumes(self, factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Factor must be a number")
        for key in self.data:
            self.data[key] *= factor

    def get_volume(self, key):
        return self.data.get(key, None)

if __name__ == '__main__':
    volume_data = VolumeData()
    volume_data.add_volume('room', 100)
    volume_data.add_volume('garage', 200)
    print("Original volumes:", volume_data.data)
    
    volume_data.scale_volumes(2)
    print("Scaled volumes:", volume_data.data)
    
    print("Volume of room after scaling:", volume_data.get_volume('room'))
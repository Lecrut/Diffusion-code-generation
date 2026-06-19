class VolumeData:
    def __init__(self):
        self.data = {}

    def add_volume(self, key, value):
        self.data[key] = value

    def scale_volumes(self, factor):
        for key in self.data:
            self.data[key] *= factor

    def get_volume(self, key):
        return self.data.get(key, None)

if __name__ == '__main__':
    volume_data = VolumeData()
    volume_data.add_volume('room1', 50)
    volume_data.add_volume('room2', 75)
    print("Original volumes:", volume_data.data)
    
    scale_factor = 2
    volume_data.scale_volumes(scale_factor)
    print(f"Volumes after scaling by {scale_factor}:", volume_data.data)
    
    print("Volume of room1:", volume_data.get_volume('room1'))
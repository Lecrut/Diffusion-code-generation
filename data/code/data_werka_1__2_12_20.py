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
    volume_data.add_volume('room', 100)
    volume_data.add_volume('garage', 200)
    
    print("Original volumes:")
    print(f"Room: {volume_data.get_volume('room')}")
    print(f"Garage: {volume_data.get_volume('garage')}")
    
    volume_data.scale_volumes(1.5)
    
    print("\nScaled volumes:")
    print(f"Room: {volume_data.get_volume('room')}")
    print(f"Garage: {volume_data.get_volume('garage')}")
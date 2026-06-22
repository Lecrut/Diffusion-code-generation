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
    volume_data.add_volume('cube', 27)
    volume_data.add_volume('sphere', 52.36)
    
    print("Original volumes:")
    print(f"Cube: {volume_data.get_volume('cube')}")
    print(f"Sphere: {volume_data.get_volume('sphere')}")
    
    volume_data.scale_volumes(2)
    
    print("\nScaled volumes by a factor of 2:")
    print(f"Cube: {volume_data.get_volume('cube')}")
    print(f"Sphere: {volume_data.get_volume('sphere')}")
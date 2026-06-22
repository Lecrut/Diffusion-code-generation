class VolumeData:
    def __init__(self):
        self.data = {}

    def add_volume(self, key, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Volume must be a number")
        self.data[key] = value

    def get_volume(self, key):
        return self.data.get(key, None)

    def scale_volumes(self, factor):
        for key in self.data:
            self.data[key] *= factor

if __name__ == '__main__':
    volume_data = VolumeData()
    volume_data.add_volume('room1', 50.0)
    volume_data.add_volume('room2', 75.0)
    print("Original volumes:", volume_data.data)

    scale_factor = 2
    volume_data.scale_volumes(scale_factor)
    print(f"Volumes after scaling by {scale_factor}:", volume_data.data)
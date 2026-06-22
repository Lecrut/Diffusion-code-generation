class VolumeData:
    def __init__(self, data):
        self.data = data

    def scale(self, factor):
        return [x * factor for x in self.data]

    def get_data(self):
        return self.data

if __name__ == '__main__':
    sample_data = [1.0, 2.5, 3.75, 4.0]
    volume_data = VolumeData(sample_data)
    scaled_data = volume_data.scale(2.0)
    print(scaled_data)
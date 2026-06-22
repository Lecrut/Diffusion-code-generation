class VolumeData:
    def __init__(self, data):
        self.data = data

    def scale(self, factor):
        return [x * factor for x in self.data]

def main():
    sample_data = [1.0, 2.5, 3.7, 4.8]
    volume = VolumeData(sample_data)
    scaled_volume = volume.scale(2.0)
    print(scaled_volume)

if __name__ == '__main__':
    main()
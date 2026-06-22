class VolumeData:
    def __init__(self, volumes):
        self.volumes = volumes

    def scale_volumes(self, factor):
        return [volume * factor for volume in self.volumes]

if __name__ == '__main__':
    sample_volumes = [10.0, 20.0, 30.0, 40.0, 50.0]
    volume_data = VolumeData(sample_volumes)
    scale_factor = 2
    scaled_volumes = volume_data.scale_volumes(scale_factor)
    print(scaled_volumes)
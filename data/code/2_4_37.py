class VolumeScaler:
    def __init__(self, volumes):
        self.volumes = volumes

    def scale(self, factor):
        return [volume * factor for volume in self.volumes]

if __name__ == '__main__':
    initial_volumes = [10.2, 20.5, 30.7]
    scaling_factor = 1.5
    scaler = VolumeScaler(initial_volumes)
    scaled_volumes = scaler.scale(scaling_factor)
    print(scaled_volumes)
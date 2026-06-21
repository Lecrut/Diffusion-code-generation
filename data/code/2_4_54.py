class VolumeScaler:
    def __init__(self, volumes):
        if not all(isinstance(volume, (int, float)) for volume in volumes):
            raise ValueError("All elements in volumes must be numbers.")
        self.volumes = volumes

    def scale(self, factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Factor must be a number.")
        return [float(volume) * float(factor) for volume in self.volumes]

if __name__ == '__main__':
    initial_volumes = [5.0, 6.2, 7.8]
    scaling_factor = 1.2
    scaler = VolumeScaler(initial_volumes)
    scaled_volumes = scaler.scale(scaling_factor)
    print(scaled_volumes)
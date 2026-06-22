import numpy as np

class VolumeScaler:
    def __init__(self, factor):
        self.factor = factor

    def scale(self, volumes):
        return volumes * self.factor

    def compute_total_volume(self, volumes):
        return np.sum(volumes)

    def compute_average_volume(self, volumes):
        if volumes.size == 0:
            return 0.0
        return np.mean(volumes)

if __name__ == '__main__':
    volumes = np.array([10.5, 20.3, 5.1, 15.2])
    scaler = VolumeScaler(factor=2.0)
    scaled_volumes = scaler.scale(volumes)
    total = scaler.compute_total_volume(scaled_volumes)
    average = scaler.compute_average_volume(scaled_volumes)
    print(f"Scaled volumes: {scaled_volumes}")
    print(f"Total volume: {total}")
    print(f"Average volume: {average}")
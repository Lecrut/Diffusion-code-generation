import numpy as np

class VolumeScaler:
    def __init__(self, volumes):
        self.volumes = np.asarray(volumes, dtype=float)

    def scale_by_factor(self, factor):
        return self.volumes * factor

    def compute_total(self):
        return np.sum(self.volumes)

    def compute_mean(self):
        return np.mean(self.volumes)

    def normalize(self):
        total = self.compute_total()
        if total == 0:
            return np.zeros_like(self.volumes)
        return self.volumes / total

def process_volumes(volumes, scale_factor):
    scaler = VolumeScaler(volumes)
    scaled = scaler.scale_by_factor(scale_factor)
    total = scaler.compute_total()
    mean = scaler.compute_mean()
    normalized = scaler.normalize()
    return scaled, total, mean, normalized

if __name__ == '__main__':
    sample_volumes = [10.5, 20.3, 15.7, 30.1, 5.2]
    factor = 2.5
    scaled, total, mean, normalized = process_volumes(sample_volumes, factor)
    print(scaled)
    print(total)
    print(mean)
    print(normalized)
import numpy as np

class VolumeScaler:
    def __init__(self, unit_multiplier):
        self.unit_multiplier = unit_multiplier

    def scale_volumes(self, measurements):
        input_array = np.array(measurements, dtype=np.float64)
        if input_array.size == 0:
            return np.array([], dtype=np.float64)
        return input_array * self.unit_multiplier

    def calculate_total_volume(self, measurements):
        input_array = np.array(measurements, dtype=np.float64)
        if input_array.size == 0:
            return 0.0
        return np.sum(input_array)

if __name__ == '__main__':
    sample_measurements = [10.5, 20.3, 15.75, 8.2, 30.0]
    scaler = VolumeScaler(1.60934)
    scaled_volumes = scaler.scale_volumes(sample_measurements)
    total_scaled_volume = scaler.calculate_total_volume(sample_measurements)
    total_scaled_volume_scaled = np.sum(scaled_volumes)
    print(scaled_volumes)
    print(total_scaled_volume_scaled)
import numpy as np

def scale_volume_measurements(measurements, scaling_factor):
    if not isinstance(measurements, np.ndarray):
        measurements = np.array(measurements)
    if measurements.dtype not in [np.float32, np.float64, np.int32, np.int64]:
        measurements = measurements.astype(np.float64)
    scaled_data = measurements * scaling_factor
    return scaled_data

class VolumeProcessor:
    def __init__(self, raw_volumes):
        self.raw_volumes = np.array(raw_volumes, dtype=np.float64)
    
    def apply_unit_conversion(self, factor):
        if factor <= 0:
            raise ValueError("Scaling factor must be positive")
        return self.raw_volumes * factor
    
    def get_statistics(self):
        return {
            "mean": float(np.mean(self.raw_volumes)),
            "std_dev": float(np.std(self.raw_volumes)),
            "min": float(np.min(self.raw_volumes)),
            "max": float(np.max(self.raw_volumes))
        }

if __name__ == '__main__':
    sample_volumes = [10.5, 25.0, 33.7, 12.2, 45.9, 8.1]
    scale_factor = 2.0
    
    direct_scaled = scale_volume_measurements(sample_volumes, scale_factor)
    print(direct_scaled)
    
    processor = VolumeProcessor(sample_volumes)
    converted_volumes = processor.apply_unit_conversion(scale_factor)
    print(converted_volumes)
    
    stats = processor.get_statistics()
    print(stats['mean'])
    print(stats['std_dev'])
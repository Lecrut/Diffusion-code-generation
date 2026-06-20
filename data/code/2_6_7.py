import numpy as np

class VolumeScaler:
    def __init__(self, measurements):
        self.measurements = np.array(measurements, dtype=np.float64)

    def scale_by_factor(self, factor):
        return self.measurements * factor

    def convert_units(self, conversion_factor):
        return self.measurements * conversion_factor

    def compute_statistics(self):
        return {
            "mean": float(np.mean(self.measurements)),
            "std_dev": float(np.std(self.measurements)),
            "min": float(np.min(self.measurements)),
            "max": float(np.max(self.measurements))
        }

if __name__ == '__main__':
    sample_data = [10.5, 20.0, 15.25, 30.0, 45.75, 50.0, 5.0]
    scaler = VolumeScaler(sample_data)
    
    scaled_values = scaler.scale_by_factor(1.5)
    converted_values = scaler.convert_units(0.001)
    stats = scaler.compute_statistics()
    
    print("Original Measurements:")
    print(sample_data)
    print("\nScaled by 1.5:")
    print(scaled_values)
    print("\nConverted (x0.001):")
    print(converted_values)
    print("\nStatistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
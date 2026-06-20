import numpy as np

class VolumeCalculator:
    def __init__(self, volumes):
        self.volumes = np.array(volumes, dtype=np.float64)

    def scale_volumes(self, factor):
        return self.volumes * factor

    def convert_units(self, from_unit='cubic_meters', to_unit='liters'):
        conversion_factors = {
            ('cubic_meters', 'liters'): 1000.0,
            ('liters', 'cubic_meters'): 0.001,
            ('cubic_meters', 'gallons'): 264.172,
            ('gallons', 'cubic_meters'): 1 / 264.172,
            ('liters', 'gallons'): 0.264172,
            ('gallons', 'liters'): 3.78541,
        }
        if from_unit == to_unit:
            return self.volumes.copy()
        factor = conversion_factors.get((from_unit, to_unit))
        if factor is None:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
        return self.volumes * factor

    def aggregate_statistics(self):
        mean_val = np.mean(self.volumes)
        median_val = np.median(self.volumes)
        std_val = np.std(self.volumes)
        total_val = np.sum(self.volumes)
        return {
            'mean': mean_val,
            'median': median_val,
            'std': std_val,
            'total': total_val
        }

def process_volume_data():
    sample_volumes = [1.5, 2.3, 0.75, 4.0, 1.1, 3.3, 2.8, 0.9]
    calculator = VolumeCalculator(sample_volumes)
    scaled_volumes = calculator.scale_volumes(2.5)
    converted_volumes = calculator.convert_units(from_unit='cubic_meters', to_unit='liters')
    stats = calculator.aggregate_statistics()
    return {
        'original': sample_volumes,
        'scaled': scaled_volumes.tolist(),
        'converted': converted_volumes.tolist(),
        'statistics': stats
    }

if __name__ == '__main__':
    result = process_volume_data()
    print(result)
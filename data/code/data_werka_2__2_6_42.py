class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 1e-6,
            'mm3': 1e-9,
            'in3': 1.63871e-5,
            'ft3': 2.83168e-2
        }

    def convert_to_target_unit(self, volumes, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {target_unit}")
        
        total_volume = sum(volume * self.conversion_factors[unit] for volume, unit in volumes)
        return total_volume

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (2000, 'cm3'), (500000, 'mm3'), (100, 'in3'), (3, 'ft3')]
    target_unit = 'm3'
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1.0,
            'cm3': 1e-6,
            'mm3': 1e-9,
            'in3': 16.387064,
            'ft3': 28316.846592
        }

    def convert_to_target_unit(self, volumes: list[tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_volume = sum(volume * self.conversion_factors[unit] / self.conversion_factors[target_unit]
                           for volume, unit in volumes)
        return total_volume

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10.0, 'm3'), (500.0, 'cm3'), (2000.0, 'mm3'), (1.0, 'in3')]
    target_unit = 'ft3'
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
from typing import List, Tuple

class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 1e-6,
            'mm3': 1e-9,
            'dm3': 0.001,
            'ft3': 28.316846592,
            'in3': 16.387064,
        }

    def convert_to_target_unit(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_volume = sum(volume * self.conversion_factors[unit] for volume, unit in volumes)
        return total_volume / self.conversion_factors[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [
        (10, 'm3'),
        (2000, 'cm3'),
        (500000, 'mm3'),
        (1.5, 'dm3'),
        (0.1, 'ft3'),
        (1000, 'in3')
    ]
    target_unit = 'm3'
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
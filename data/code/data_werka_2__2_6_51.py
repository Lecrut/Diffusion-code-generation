from typing import List, Tuple

class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 1e-6,
            'mm3': 1e-9,
            'in3': 1.6387064e-5,
            'ft3': 2.8316846592e-2
        }

    def convert_to_target_unit(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_volume = sum(volume * self.conversion_factors[unit] for volume, unit in volumes)
        return total_volume * self.conversion_factors[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (500, 'cm3'), (2000, 'mm3'), (10, 'in3'), (0.5, 'ft3')]
    target_unit = 'm3'
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
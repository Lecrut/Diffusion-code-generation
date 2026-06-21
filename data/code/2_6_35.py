from typing import List, Tuple

class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1.0,
            'cm3': 1e-6,
            'mm3': 1e-9,
            'in3': 16.3871,
            'ft3': 28316.85
        }

    def convert_to_target_unit(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_volume = sum(volume * self.conversion_factors[unit] for volume, unit in volumes)
        return total_volume / self.conversion_factors[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (500, 'cm3'), (2000, 'mm3'), (1, 'in3')]
    target_unit = 'ft3'
    total_volume_ft3 = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume_ft3)
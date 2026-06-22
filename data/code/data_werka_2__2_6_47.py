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

    def convert_to_target_unit(self, volume: float, source_unit: str, target_unit: str) -> float:
        if source_unit not in self.conversion_factors or target_unit not in self.conversion_factors:
            raise ValueError("Unsupported unit")
        return volume * self.conversion_factors[source_unit] / self.conversion_factors[target_unit]

    def total_volume(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        return sum(self.convert_to_target_unit(volume, unit, target_unit) for volume, unit in volumes)

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (500, 'cm3'), (2000, 'mm3'), (10, 'in3'), (0.1, 'ft3')]
    target_unit = 'm3'
    total_volume_in_target_unit = calculator.total_volume(sample_volumes, target_unit)
    print(total_volume_in_target_unit)
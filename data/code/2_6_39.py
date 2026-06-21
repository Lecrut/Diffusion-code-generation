from typing import List, Tuple

class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 1e-6,
            'dm3': 0.001,
            'ft3': 28.316846592,
            'in3': 1.6387064e-5
        }

    def convert_to_base(self, volume: float, unit: str) -> float:
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return volume * self.conversion_factors[unit]

    def total_volume(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        base_volumes = [self.convert_to_base(volume, unit) for volume, unit in volumes]
        total_in_target = sum(base_volumes) / self.conversion_factors[target_unit]
        return total_in_target

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (2000, 'cm3'), (5, 'dm3'), (100, 'ft3'), (1000, 'in3')]
    target_unit = 'm3'
    total_volume = calculator.total_volume(sample_volumes, target_unit)
    print(total_volume)
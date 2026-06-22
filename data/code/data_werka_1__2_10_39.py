from typing import List, Tuple

class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 1e-6,
            'dm3': 0.001,
            'ft3': 0.0283168,
            'in3': 1.63871e-5
        }

    def convert_to_m3(self, volume: float, unit: str) -> float:
        return volume * self.conversion_factors[unit]

    def total_volume_in_target_unit(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        total_volume_m3 = sum(self.convert_to_m3(volume, unit) for volume, unit in volumes)
        return total_volume_m3 / self.conversion_factors[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (500, 'cm3'), (2, 'dm3'), (100, 'ft3'), (1000, 'in3')]
    target_unit = 'm3'
    total_volume = calculator.total_volume_in_target_unit(sample_volumes, target_unit)
    print(total_volume)
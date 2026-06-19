from typing import List, Tuple

class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 0.000001,
            'mm3': 0.000000001,
            'dm3': 0.001,
            'km3': 1e9,
            'in3': 6.10237440947e-8,
            'ft3': 2.8316846592e-5,
            'yd3': 0.764554857984
        }

    def convert_to_target_unit(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        total_volume = sum(volume * self.conversion_factors[unit] for volume, unit in volumes if unit in self.conversion_factors)
        return total_volume / self.conversion_factors[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (2000, 'cm3'), (500000, 'mm3'), (1.5, 'dm3')]
    target_unit = 'm3'
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
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

    def validate_unit(self, unit: str) -> None:
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")

    def convert_to_m3(self, volume: float, unit: str) -> float:
        self.validate_unit(unit)
        return volume * self.conversion_factors[unit]

    def total_volume_in_target_unit(self, volumes: List[Tuple[float, str]], target_unit: str) -> float:
        self.validate_unit(target_unit)
        total_volume_m3 = sum(self.convert_to_m3(volume, unit) for volume, unit in volumes)
        return total_volume_m3 / self.conversion_factors[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (500, 'cm3'), (2000, 'mm3'), (1, 'in3')]
    target_unit = 'ft3'
    result = calculator.total_volume_in_target_unit(sample_volumes, target_unit)
    print(result)
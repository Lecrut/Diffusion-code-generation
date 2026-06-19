class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 0.000001,
            'dm3': 0.001,
            'mm3': 0.000000001,
            'in3': 0.0163871,
            'ft3': 28.3168,
            'yd3': 764.555
        }

    def convert_to_target_unit(self, volumes: list[tuple[float, str]], target_unit: str) -> float:
        total_volume = sum(volume * self.conversion_factors[source_unit] / self.conversion_factors[target_unit]
                           for volume, source_unit in volumes)
        return total_volume

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (2000, 'cm3'), (5, 'dm3'), (8000000, 'mm3'),
                      (100, 'in3'), (2, 'ft3'), (0.5, 'yd3')]
    target_unit = 'm3'
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
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
        total_volume = sum(volume * self.conversion_factors[unit] for volume, unit in volumes if unit in self.conversion_factors)
        return total_volume / self.conversion_factors[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (2000, 'cm3'), (5, 'ft3')]
    target_unit = 'dm3'
    result = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(result)
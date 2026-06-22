class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 1e-6,
            'dm3': 0.001,
            'ft3': 0.0283168,
            'in3': 1.63871e-5
        }

    def total_volume(self, volumes: list[tuple[float, str]], target_unit: str) -> float:
        return sum(
            volume * self.conversion_factors[unit] / self.conversion_factors[target_unit]
            for volume, unit in volumes
        )

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [
        (10.0, 'm3'),
        (2000.0, 'cm3'),
        (5.0, 'dm3'),
        (150.0, 'ft3'),
        (100000.0, 'in3')
    ]
    target_unit = 'm3'
    print(calculator.total_volume(sample_volumes, target_unit))
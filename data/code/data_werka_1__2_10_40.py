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

    def convert_to_target_unit(self, volumes: list[tuple[float, str]], target_unit: str) -> float:
        return sum(volume * self.conversion_factors[source_unit] / self.conversion_factors[target_unit]
                   for volume, source_unit in volumes)

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [(10, 'm3'), (2000, 'cm3'), (500000, 'mm3')]
    target_unit = 'ft3'
    total_volume_ft3 = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume_ft3)
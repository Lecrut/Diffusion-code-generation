class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            'm3': 1,
            'cm3': 1e-6,
            'dm3': 1e-3,
            'ft3': 28.316846592,
            'in3': 1.6387064e-5
        }

    def convert_to_target_unit(self, volumes: list[tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")

        total_volume = sum(
            volume * self.conversion_factors[unit] / self.conversion_factors[target_unit]
            for volume, unit in volumes
        )
        return total_volume

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [
        (10.0, 'm3'),
        (2000.0, 'cm3'),
        (5.0, 'dm3'),
        (100.0, 'ft3'),
        (100000.0, 'in3')
    ]
    target_unit = 'm3'
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
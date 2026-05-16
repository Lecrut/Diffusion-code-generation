class VolumeCalculator:
    def convert_to_target(self, volume, unit, target_unit):
        if unit == target_unit:
            return volume
        conversion_factors = {
            ('m3', 'L'): 1000,
            ('L', 'm3'): 0.001,
            ('m3', 'cm3'): 1000000,
            ('cm3', 'm3'): 1e-6,
            ('m3', 'in3'): 16387,
            ('in3', 'm3'): 1/16387
        }
        key = (unit, target_unit)
        if key in conversion_factors:
            return volume * conversion_factors[key]
        raise ValueError(f"Unsupported unit conversion: {unit} to {target_unit}")
    def calculate_total_volume(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        total_volume = 0.0
        for volume, unit in measurements:
            if unit == target_unit:
                total_volume += volume
            else:
                try:
                    converted_volume = self.convert_to_target(volume, unit, target_unit)
                    total_volume += converted_volume
                except ValueError as e:
                    print(f"Error processing {volume} {unit}: {e}")
        return total_volume
if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        (10.0, 'm3'),
        (500.0, 'L'),
        (2000000.0, 'cm3'),
        (1.0, 'm3')
    ]
    target = 'L'
    total = calculator.calculate_total_volume(sample_measurements, target)
    print(f"Total volume in {target}: {total}")
class VolumeCalculator:
    def convert_to_target(self, volume, from_unit, to_unit):
        if from_unit == to_unit:
            return volume
        if from_unit == 'm3' and to_unit == 'liters':
            return volume * 1000
        if from_unit == 'liters' and to_unit == 'm3':
            return volume / 1000
        if from_unit == 'cm3' and to_unit == 'liters':
            return volume / 1000
        if from_unit == 'liters' and to_unit == 'cm3':
            return volume * 1000
        return volume
    def calculate_total_volume(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        total_volume = 0.0
        for volume, unit in measurements:
            converted_volume = self.convert_to_target(volume, unit, target_unit)
            total_volume += converted_volume
        return total_volume
if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        (1.5, 'm3'),
        (5000.0, 'cm3'),
        (2.5, 'liters'),
        (0.01, 'm3')
    ]
    target = 'liters'
    total = calculator.calculate_total_volume(sample_measurements, target)
    print(total)
class VolumeCalculator:
    def convert_to_target_unit(self, volume, from_unit, to_unit):
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
        if from_unit == 'm3' and to_unit == 'cm3':
            return volume * 1000000
        if from_unit == 'cm3' and to_unit == 'm3':
            return volume / 1000000
        return volume
    def calculate_total_volume(self, volumes: list[tuple[float, str]], target_unit: str) -> float:
        total_volume = 0.0
        for volume, unit in volumes:
            converted_volume = self.convert_to_target_unit(volume, unit, target_unit)
            total_volume += converted_volume
        return total_volume
if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [
        (1.5, 'm3'),
        (5000.0, 'cm3'),
        (2.5, 'liters'),
        (0.001, 'm3')
    ]
    target = 'liters'
    total = calculator.calculate_total_volume(sample_volumes, target)
    print(total)
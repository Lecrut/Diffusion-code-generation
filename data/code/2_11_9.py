class VolumeCalculator:
    def convert_to_target_unit(self, volume, from_unit, to_unit):
        if from_unit == to_unit:
            return volume
        if from_unit == "m^3" and to_unit == "L":
            return volume * 1000
        if from_unit == "L" and to_unit == "m^3":
            return volume / 1000
        if from_unit == "cm^3" and to_unit == "L":
            return volume / 1000
        if from_unit == "L" and to_unit == "cm^3":
            return volume * 1000000
        return volume
    def calculate_total_volume(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        total_volume = 0.0
        for volume, unit in measurements:
            converted_volume = self.convert_to_target_unit(volume, unit, target_unit)
            total_volume += converted_volume
        return total_volume
if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        (10.0, "m^3"),
        (500.0, "L"),
        (250000.0, "cm^3"),
        (0.5, "L")
    ]
    target = "L"
    total = calculator.calculate_total_volume(sample_measurements, target)
    print(total)
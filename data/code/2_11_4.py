class VolumeCalculator:
    def convert_to_target(self, volume, unit, target_unit):
        if unit == target_unit:
            return volume
        if unit == "m^3" and target_unit == "L":
            return volume * 1000
        if unit == "L" and target_unit == "m^3":
            return volume / 1000
        if unit == "cm^3" and target_unit == "L":
            return volume / 1000
        if unit == "m^3" and target_unit == "cm^3":
            return volume * 1000000
        if unit == "L" and target_unit == "cm^3":
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
        (1.5, "m^3"),
        (200.0, "L"),
        (5000.0, "cm^3"),
        (0.5, "m^3")
    ]
    target = "L"
    total = calculator.calculate_total_volume(sample_measurements, target)
    print(total)
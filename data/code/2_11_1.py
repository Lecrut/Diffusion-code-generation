class VolumeCalculator:
    def convert_to_target(self, volume, unit, target_unit):
        if unit == target_unit:
            return volume
        if unit == "m^3" and target_unit == "liters":
            return volume * 1000
        if unit == "liters" and target_unit == "m^3":
            return volume / 1000
        if unit == "cm^3" and target_unit == "liters":
            return volume / 1000
        if unit == "liters" and target_unit == "cm^3":
            return volume * 1000
        return volume
    def calculate_total_volume(self, volume_list: list[tuple[float, str]], target_unit: str) -> float:
        total_volume = 0.0
        for volume, unit in volume_list:
            converted_volume = self.convert_to_target(volume, unit, target_unit)
            total_volume += converted_volume
        return total_volume
if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_volumes = [
        (1.5, "m^3"),
        (500.0, "liters"),
        (10000.0, "cm^3"),
        (2.0, "liters")
    ]
    target = "liters"
    total = calculator.calculate_total_volume(sample_volumes, target)
    print(f"Total volume in {target}: {total}")
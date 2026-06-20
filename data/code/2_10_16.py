class VolumeCalculator:
    UNIT_CONVERSION_TO_LITERS = {
        'ml': 0.001,
        'l': 1.0,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'fl_oz': 0.0295735,
        'm3': 1000.0,
        'cm3': 0.001,
        'in3': 0.0163871,
        'ft3': 28.3168,
    }

    def __init__(self):
        self.volumes = []

    def add_volume(self, value: float, unit: str) -> None:
        lower_unit = unit.lower().strip()
        if lower_unit not in self.UNIT_CONVERSION_TO_LITERS:
            raise ValueError(f"Unsupported unit: {unit}")
        self.volumes.append((value, lower_unit))

    def add_volumes(self, volumes: list[tuple[float, str]]) -> None:
        for value, unit in volumes:
            self.add_volume(value, unit)

    def get_total(self, target_unit: str) -> float:
        lower_target = target_unit.lower().strip()
        if lower_target not in self.UNIT_CONVERSION_TO_LITERS:
            raise ValueError(f"Unsupported target unit: {target_unit}")

        total_in_liters = sum(
            value * self.UNIT_CONVERSION_TO_LITERS[unit]
            for value, unit in self.volumes
        )

        result = total_in_liters / self.UNIT_CONVERSION_TO_LITERS[lower_target]
        return result

if __name__ == '__main__':
    calculator = VolumeCalculator()
    calculator.add_volumes([
        (1000, 'ml'),
        (1, 'l'),
        (1, 'gal'),
        (500, 'cm3'),
    ])
    total_liters = calculator.get_total('l')
    total_gallons = calculator.get_total('gal')
    print(total_liters)
    print(total_gallons)
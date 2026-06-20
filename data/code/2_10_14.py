class VolumeCalculator:
    CONVERSION_TO_LITERS = {
        'ml': 0.001,
        'l': 1.0,
        'm3': 1000.0,
        'cm3': 0.001,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'floz': 0.0295735,
        'tbsp': 0.0147868,
        'tsp': 0.00492892,
    }

    def calculate_total(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        total_liters = sum(
            amount * self.CONVERSION_TO_LITERS[unit.lower()]
            for amount, unit in measurements
        )
        return total_liters / self.CONVERSION_TO_LITERS[target_unit.lower()]

if __name__ == '__main__':
    calc = VolumeCalculator()
    volumes = [(1000, 'ml'), (2, 'l'), (0.5, 'gal')]
    result = calc.calculate_total(volumes, 'l')
    print(result)
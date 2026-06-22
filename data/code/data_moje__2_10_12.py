class VolumeCalculator:
    CONVERSION_TO_LITERS = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon_us': 3.78541,
        'quart_us': 0.946353,
        'pint_us': 0.473176,
        'cup_us': 0.236588,
        'fluid_ounce_us': 0.0295735,
        'tablespoon_us': 0.0147868,
        'teaspoon_us': 0.00492892,
        'imperial_gallon': 4.54609,
        'imperial_quart': 1.13652,
        'imperial_pint': 0.568261,
        'imperial_cup': 0.284131,
        'imperial_fluid_ounce': 0.0284131,
        'imperial_tablespoon': 0.0177582,
        'imperial_teaspoon': 0.00591939,
        'cubic_centimeter': 0.001,
        'cubic_foot': 28.3168,
        'cubic_inch': 0.0163871
    }

    def __init__(self):
        self.measurements = []

    def calculate_total_volume(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        if not measurements:
            return 0.0

        target_unit_lower = target_unit.lower().strip()
        if target_unit_lower not in self.CONVERSION_TO_LITERS:
            raise ValueError(f"Unknown target unit: {target_unit}")

        total_liters = sum(
            volume * self.CONVERSION_TO_LITERS[unit.lower().strip()]
            for volume, unit in measurements
            if unit.lower().strip() in self.CONVERSION_TO_LITERS
        )

        result = total_liters / self.CONVERSION_TO_LITERS[target_unit_lower]
        return result

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        (2.0, 'liter'),
        (1.0, 'gallon_us'),
        (500.0, 'milliliter'),
        (3.0, 'cubic_meter')
    ]
    target = 'liter'
    total = calculator.calculate_total_volume(sample_measurements, target)
    print(total)
class VolumeCalculator:
    CONVERSION_TO_LITERS = {
        'ml': 0.001,
        'l': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'floz': 0.0295735
    }

    def calculate_total_volume(self, measurements: list, target_unit: str) -> float:
        if not measurements:
            return 0.0
        target_unit_lower = target_unit.lower()
        if target_unit_lower not in self.CONVERSION_TO_LITERS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_in_liters = sum(
            value * self.CONVERSION_TO_LITERS[unit.lower()]
            for value, unit in measurements
        )
        
        return total_in_liters / self.CONVERSION_TO_LITERS[target_unit_lower]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        (1000, 'ml'),
        (2.5, 'l'),
        (0.5, 'gal')
    ]
    result = calculator.calculate_total_volume(sample_measurements, 'l')
    print(result)
class VolumeCalculator:
    UNIT_CONVERSIONS = {
        'ml': 1.0,
        'l': 1000.0,
        'gal': 3785.41,
        'pt': 473.176,
        'ft3': 28316.85,
        'in3': 16.3871,
    }

    def calculate_total_volume(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_ml = sum(
            value * self.UNIT_CONVERSIONS[unit] 
            for value, unit in measurements 
            if unit in self.UNIT_CONVERSIONS
        )
        
        return total_ml / self.UNIT_CONVERSIONS[target_unit]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [(1.0, 'l'), (500.0, 'ml'), (0.5, 'gal'), (1000.0, 'pt')]
    result = calculator.calculate_total_volume(sample_measurements, 'ml')
    print(result)
    result_ft3 = calculator.calculate_total_volume(sample_measurements, 'ft3')
    print(result_ft3)
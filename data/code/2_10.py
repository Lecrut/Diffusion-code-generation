class VolumeCalculator:
    CONVERSION_TO_M3 = {
        'm3': 1.0,
        'l': 0.001,
        'ml': 0.000001,
        'gal': 0.00378541,
        'qt': 0.000946353,
        'pt': 0.000473176,
        'cup': 0.000236588,
        'fl_oz': 0.0000295735,
        'ft3': 0.0283168,
        'in3': 0.0000163871
    }

    def calculate_total_volume(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.CONVERSION_TO_M3:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        target_factor = self.CONVERSION_TO_M3[target_unit]
        
        total_m3 = sum(
            volume * self.CONVERSION_TO_M3[unit]
            for volume, unit in measurements
            if unit in self.CONVERSION_TO_M3
        )
        
        return total_m3 / target_factor

if __name__ == '__main__':
    calculator = VolumeCalculator()
    measurements = [
        (1.0, 'l'),
        (500.0, 'ml'),
        (1.0, 'gal'),
        (2.0, 'ft3')
    ]
    result = calculator.calculate_total_volume(measurements, 'l')
    print(result)
class VolumeCalculator:
    BASE_TO_ML = {
        'ml': 1.0,
        'l': 1000.0,
        'gal': 3785.411784,
        'qt': 946.352946,
        'pt': 473.176473,
        'cup': 236.5882365,
        'fl_oz': 29.57352956,
        'in3': 16.387064,
        'ft3': 28316.846592,
        'm3': 1000000.0
    }

    def total_volume(self, measurements: list[tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.BASE_TO_ML:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_ml = sum(
            value * self.BASE_TO_ML.get(unit, 0.0)
            for value, unit in measurements
        )
        
        return total_ml / self.BASE_TO_ML[target_unit]

if __name__ == '__main__':
    calc = VolumeCalculator()
    data = [
        (5.0, 'l'),
        (500.0, 'ml'),
        (1.0, 'gal'),
        (10.0, 'cup')
    ]
    result_liters = calc.total_volume(data, 'l')
    print(result_liters)
    
    result_gallons = calc.total_volume(data, 'gal')
    print(result_gallons)
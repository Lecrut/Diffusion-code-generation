from typing import List, Dict, Any

class VolumeCalculator:
    _conversion_factors: Dict[str, float] = {
        'ml': 1.0,
        'l': 1000.0,
        'us_gal': 3785.411784,
        'imp_gal': 4546.09,
        'ft3': 28316.846592,
        'in3': 16.387064,
    }

    def calculate_total(self, measurements: List[Dict[str, Any]], target_unit: str) -> float:
        if target_unit not in self._conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_ml = sum(
            value * self._conversion_factors[unit]
            for value, unit in measurements
            if unit in self._conversion_factors
        )
        
        return total_ml / self._conversion_factors[target_unit]

if __name__ == '__main__':
    sample_data = [
        (500, 'ml'),
        (1.5, 'l'),
        (2, 'us_gal'),
        (1000, 'ml'),
    ]
    calculator = VolumeCalculator()
    result = calculator.calculate_total(sample_data, 'l')
    print(result)
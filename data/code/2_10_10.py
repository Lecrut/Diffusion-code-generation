from typing import List, Tuple, Dict
from decimal import Decimal

class VolumeCalculator:
    CONVERSION_RATES: Dict[str, float] = {
        'ml': 1.0,
        'l': 1000.0,
        'm3': 1000000.0,
        'gal_us': 3785.41,
        'fl_oz_us': 29.5735,
        'qt_us': 946.353,
        'pt_us': 473.176,
        'cup_us': 236.588,
        'tbsp_us': 14.7868,
        'tsp_us': 4.92892,
    }

    def calculate_total_volume(self, measurements: List[Tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.CONVERSION_RATES:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_ml = sum(
            amount * self.CONVERSION_RATES[unit]
            for amount, unit in measurements
        )
        
        target_rate = self.CONVERSION_RATES[target_unit]
        return total_ml / target_rate

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        (500.0, 'ml'),
        (1.5, 'l'),
        (33.814, 'fl_oz_us'),
        (0.25, 'gal_us'),
    ]
    result = calculator.calculate_total_volume(sample_measurements, 'ml')
    print(f"Total volume: {result} ml")
    result_liters = calculator.calculate_total_volume(sample_measurements, 'l')
    print(f"Total volume: {result_liters} l")
    result_gallons = calculator.calculate_total_volume(sample_measurements, 'gal_us')
    print(f"Total volume: {result_gallons} gal_us")
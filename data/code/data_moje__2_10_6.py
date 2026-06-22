from typing import List, Tuple, Dict, Union

class VolumeCalculator:
    CONVERSION_FACTORS: Dict[str, float] = {
        'milliliter': 1.0,
        'liter': 1000.0,
        'gallon': 3785.41,
        'quart': 946.353,
        'pint': 473.176,
        'fluid_ounce': 29.5735,
        'cup': 236.588,
        'cubic_meter': 1000000.0,
        'cubic_centimeter': 1.0,
        'barrel_oil': 158987.0,
    }

    def calculate_total_volume(self, measurements: List[Tuple[float, str]], target_unit: str) -> float:
        if target_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_ml = sum(
            value * self.CONVERSION_FACTORS[unit.lower()]
            for value, unit in measurements
            if unit.lower() in self.CONVERSION_FACTORS
        )
        
        return total_ml / self.CONVERSION_FACTORS[target_unit.lower()]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        (500, 'milliliter'),
        (2, 'liter'),
        (1, 'gallon'),
        (16, 'fluid_ounce'),
        (1, 'quart'),
        (1000, 'cubic_centimeter'),
        (0.5, 'barrel_oil')
    ]
    result = calculator.calculate_total_volume(sample_measurements, 'liter')
    print(f"Total volume in liters: {result}")
    
    result_cups = calculator.calculate_total_volume(sample_measurements, 'cup')
    print(f"Total volume in cups: {result_cups}")
    
    result_gallons = calculator.calculate_total_volume(sample_measurements, 'gallon')
    print(f"Total volume in gallons: {result_gallons}")
from typing import List, Dict, Optional, Union

class VolumeCalculator:
    CONVERSION_FACTORS: Dict[str, float] = {
        "l": 1.0,
        "ml": 0.001,
        "gal": 3.78541,
        "qt": 0.946353,
        "pt": 0.473176,
        "fl_oz": 0.0295735,
        "m3": 1000.0,
        "cm3": 0.001,
    }

    def convert_to_target(self, measurements: List[Dict[str, Union[int, float]]], target_unit: str) -> float:
        if target_unit.lower() not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_liters = sum(
            entry["value"] * self.CONVERSION_FACTORS[entry["unit"].lower()]
            for entry in measurements
        )
        
        target_factor = self.CONVERSION_FACTORS[target_unit.lower()]
        return total_liters / target_factor

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_data = [
        {"value": 2, "unit": "l"},
        {"value": 500, "unit": "ml"},
        {"value": 1, "unit": "gal"},
        {"value": 128, "unit": "fl_oz"}
    ]
    result_gallons = calculator.convert_to_target(sample_data, "gal")
    result_liters = calculator.convert_to_target(sample_data, "l")
    print(f"Total in gallons: {result_gallons}")
    print(f"Total in liters: {result_liters}")
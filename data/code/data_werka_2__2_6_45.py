from typing import List, Dict

class VolumeCalculator:
    def __init__(self):
        self.conversion_factors: Dict[str, float] = {
            'm3': 1.0,
            'cm3': 1e-6,
            'mm3': 1e-9,
            'in3': 16.3871,
            'ft3': 28316.85
        }

    def convert_to_target_unit(self, volumes: List[Dict[str, float]], target_unit: str) -> float:
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")

        total_volume = sum(
            volume['value'] * self.conversion_factors[volume['unit']]
            for volume in volumes
        )

        return total_volume / self.conversion_factors[target_unit]

if __name__ == '__main__':
    sample_volumes = [
        {'value': 10, 'unit': 'm3'},
        {'value': 2000, 'unit': 'cm3'},
        {'value': 500000, 'unit': 'mm3'},
        {'value': 100, 'unit': 'in3'},
        {'value': 1, 'unit': 'ft3'}
    ]
    target_unit = 'm3'
    
    calculator = VolumeCalculator()
    total_volume = calculator.convert_to_target_unit(sample_volumes, target_unit)
    print(total_volume)
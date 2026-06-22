class VolumeCalculator:
    def __init__(self):
        self.conversion_to_liters = {
            'milliliter': 0.001,
            'liter': 1.0,
            'gallon': 3.78541,
            'quart': 0.946353,
            'pint': 0.473176,
            'cup': 0.236588,
            'fluid_ounce': 0.0295735,
            'tablespoon': 0.0147868,
            'teaspoon': 0.00492892,
            'cubic_meter': 1000.0,
            'cubic_centimeter': 0.001,
        }

    def convert_volume(self, measurements, target_unit):
        target_lower = target_unit.lower()
        if target_lower not in self.conversion_to_liters:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_liters = sum(
            value * self.conversion_to_liters[unit.lower()]
            for value, unit in measurements
        )
        
        return total_liters / self.conversion_to_liters[target_lower]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    measurements = [
        (1000, 'milliliter'),
        (2, 'liter'),
        (1, 'gallon'),
        (500, 'cubic_centimeter')
    ]
    result = calculator.convert_volume(measurements, 'liter')
    print(result)
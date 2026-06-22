class VolumeCalculator:
    CONVERSION_FACTORS = {
        'ml': 1.0,
        'l': 1000.0,
        'gal': 3785.41,
        'qt': 946.353,
        'pt': 473.176,
        'cup': 236.588,
        'tbsp': 14.787,
        'tsp': 4.929,
        'ft3': 28316.8,
        'm3': 1000000.0,
    }

    def __init__(self):
        self.measurements = []

    def add_measurement(self, value, unit):
        unit_lower = unit.lower()
        if unit_lower not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {unit}")
        self.measurements.append((value, unit_lower))

    def calculate_total(self, target_unit):
        target_lower = target_lower = target_unit.lower()
        if target_lower not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_ml = sum(
            value * self.CONVERSION_FACTORS[unit] 
            for value, unit in self.measurements
        )
        
        return total_ml / self.CONVERSION_FACTORS[target_lower]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    calculator.add_measurement(1, 'l')
    calculator.add_measurement(500, 'ml')
    calculator.add_measurement(0.5, 'gal')
    
    total_in_ml = calculator.calculate_total('ml')
    total_in_l = calculator.calculate_total('l')
    total_in_gal = calculator.calculate_total('gal')
    
    print(f"Total in ml: {total_in_ml}")
    print(f"Total in l: {total_in_l}")
    print(f"Total in gal: {total_in_gal}")
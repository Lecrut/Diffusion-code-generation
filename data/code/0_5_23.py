class UnitConverter:
    def __init__(self):
        self.conversions = {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.344,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.conversions[from_unit]
        result = base_value / self.conversions[to_unit]
        return result

if __name__ == '__main__':
    converter = UnitConverter()
    
    km_to_m = converter.convert(5, 'kilometer', 'meter')
    print(f"5 kilometers is {km_to_m} meters")
    
    inches_to_cm = converter.convert(10, 'inch', 'centimeter')
    print(f"10 inches is {inches_to_cm} centimeters")
    
    miles_to_km = converter.convert(1, 'mile', 'kilometer')
    print(f"1 mile is {miles_to_km} kilometers")
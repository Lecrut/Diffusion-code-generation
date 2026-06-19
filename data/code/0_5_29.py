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
            'gram': 1.0,
            'kilogram': 1000.0,
            'milligram': 0.001,
            'pound': 453.59237,
            'ounce': 28.349523125,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.conversions[from_unit]
        result = base_value / self.conversions[to_unit]
        return result

def main():
    converter = UnitConverter()
    
    length_meters = converter.convert(1, 'mile', 'kilometer')
    print(f"1 mile is {length_meters} kilometers")
    
    weight_kg = converter.convert(1, 'pound', 'kilogram')
    print(f"1 pound is {weight_kg} kilograms")
    
    distance_cm = converter.convert(5.28, 'foot', 'centimeter')
    print(f"5.28 feet is {distance_cm} centimeters")

if __name__ == '__main__':
    main()
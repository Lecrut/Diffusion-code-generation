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
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon': 3.785411784,
            'quart': 0.946352946,
            'pint': 0.473176473,
            'cup': 0.2365882365,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.conversions[from_unit]
        result = base_value / self.conversions[to_unit]
        return result

    def get_supported_units(self):
        return list(self.conversions.keys())

def main():
    converter = UnitConverter()
    
    length_result = converter.convert(1, 'mile', 'kilometer')
    print(f"1 mile = {length_result} kilometers")
    
    weight_result = converter.convert(1, 'pound', 'kilogram')
    print(f"1 pound = {weight_result} kilograms")
    
    volume_result = converter.convert(1, 'gallon', 'liter')
    print(f"1 gallon = {volume_result} liters")
    
    small_length = converter.convert(100, 'centimeter', 'inch')
    print(f"100 centimeters = {small_length} inches")

if __name__ == '__main__':
    main()
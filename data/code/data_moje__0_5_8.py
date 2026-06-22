class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.factors = {}
    
    def register_unit(self, name, factor_to_base):
        self.factors[name] = factor_to_base
    
    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.factors[from_unit]
        result = base_value / self.factors[to_unit]
        return result

if __name__ == '__main__':
    converter = UnitConverter('meter')
    converter.register_unit('meter', 1.0)
    converter.register_unit('kilometer', 1000.0)
    converter.register_unit('centimeter', 0.01)
    converter.register_unit('inch', 0.0254)
    converter.register_unit('foot', 0.3048)
    
    kilometers_to_inches = converter.convert(1.5, 'kilometer', 'inch')
    centimeters_to_feet = converter.convert(300.0, 'centimeter', 'foot')
    inches_to_meters = converter.convert(12.0, 'inch', 'meter')
    
    print(kilometers_to_inches)
    print(centimeters_to_feet)
    print(inches_to_meters)
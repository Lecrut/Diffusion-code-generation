class VolumeConverter:
    def __init__(self):
        self.factors = {
            "ml": 1.0,
            "l": 1000.0,
            "gal": 3785.411784,
            "qt": 946.352946,
            "pt": 473.176473,
            "cup": 236.5882365,
            "fl_oz": 29.5735295625,
            "tbsp": 14.78676478125,
            "tsp": 4.92892159375,
            "m3": 1000000.0,
            "cm3": 1.0,
            "ft3": 28316.846592,
            "in3": 16.387064
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        base_value = value * self.factors[from_unit]
        result = base_value / self.factors[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    
    result1 = converter.convert(1, "l", "ml")
    print(result1)
    
    result2 = converter.convert(1, "m3", "gal")
    print(result2)
    
    result3 = converter.convert(1, "gal", "l")
    print(result3)
    
    result4 = converter.convert(5, "cup", "ml")
    print(result4)
    
    result5 = converter.convert(1, "ft3", "in3")
    print(result5)
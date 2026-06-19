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
    
    val1 = 5.0
    from_u1 = 'kilometer'
    to_u1 = 'mile'
    res1 = converter.convert(val1, from_u1, to_u1)
    print(f"{val1} {from_u1} is {res1} {to_u1}")

    val2 = 100.0
    from_u2 = 'centimeter'
    to_u2 = 'inch'
    res2 = converter.convert(val2, from_u2, to_u2)
    print(f"{val2} {from_u2} is {res2} {to_u2}")

    val3 = 1.0
    from_u3 = 'mile'
    to_u3 = 'kilometer'
    res3 = converter.convert(val3, from_u3, to_u3)
    print(f"{val3} {from_u3} is {res3} {to_u3}")
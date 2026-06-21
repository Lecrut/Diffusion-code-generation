CONVERSION_FACTORS = {
    'l_to_ml': 1000,
    'l_to_gal': 0.264172,
    'ml_to_l': 0.001,
    'ml_to_gal': 0.000264172,
    'gal_to_l': 3.78541,
    'gal_to_ml': 3785.41,
    'm3_to_l': 1000,
    'm3_to_ml': 1e6,
    'm3_to_gal': 264.172,
    'l_to_m3': 0.001,
    'ml_to_m3': 1e-6,
    'gal_to_m3': 0.00378541,
}

class VolumeConverter:
    def __init__(self, conversion_factors):
        self.factors = conversion_factors

    def convert(self, from_unit, to_unit, value):
        key = f"{from_unit}_to_{to_unit}"
        if key not in self.factors:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")
        return value * self.factors[key]

    def get_supported_conversions(self):
        return list(self.factors.keys())

    def add_conversion_factor(self, from_unit, to_unit, factor):
        key = f"{from_unit}_to_{to_unit}"
        self.factors[key] = factor

    def remove_conversion_factor(self, from_unit, to_unit):
        key = f"{from_unit}_to_{to_unit}"
        if key in self.factors:
            del self.factors[key]
        else:
            raise KeyError(f"Conversion factor {key} not found")

if __name__ == '__main__':
    converter = VolumeConverter(CONVERSION_FACTORS)
    
    liters = 5
    ml_result = converter.convert('l', 'ml', liters)
    gal_result = converter.convert('l', 'gal', liters)
    
    m3 = 2
    m3_to_l_result = converter.convert('m3', 'l', m3)
    m3_to_gal_result = converter.convert('m3', 'gal', m3)
    
    gallons = 10
    gal_to_l_result = converter.convert('gal', 'l', gallons)
    
    print(ml_result)
    print(gal_result)
    print(m3_to_l_result)
    print(m3_to_gal_result)
    print(gal_to_l_result)
    
    new_factor = 0.5
    from_unit = 'barrel'
    to_unit = 'l'
    converter.add_conversion_factor(from_unit, to_unit, new_factor)
    
    barrel_to_l_result = converter.convert('barrel', 'l', 1)
    print(barrel_to_l_result)
    
    supported = converter.get_supported_conversions()
    print(len(supported))
    
    try:
        converter.convert('kg', 'lb', 5)
    except ValueError as e:
        print(str(e))
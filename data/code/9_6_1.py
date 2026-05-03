class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            "L_to_ml": 1000.0,
            "m3_to_L": 1000.0,
            "m3_to_gal": 264.172,
            "L_to_gal": 0.264172
        }
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "L" and to_unit == "ml":
            if "L_to_ml" in self.conversion_factors:
                return value * self.conversion_factors["L_to_ml"]
        elif from_unit == "m3" and to_unit == "L":
            if "m3_to_L" in self.conversion_factors:
                return value * self.conversion_factors["m3_to_L"]
        elif from_unit == "m3" and to_unit == "gal":
            if "m3_to_gal" in self.conversion_factors:
                return value * self.conversion_factors["m3_to_gal"]
        elif from_unit == "L" and to_unit == "gal":
            if "L_to_gal" in self.conversion_factors:
                return value * self.conversion_factors["L_to_gal"]
        raise ValueError(f"Conversion not supported from {from_unit} to {to_unit}")
if __name__ == '__main__':
    converter = VolumeConverter()
    test_value = 5.0
    print(f"Testing conversions for {test_value} L:")
    print(f"L to ml: {converter.convert(test_value, 'L', 'ml')}")
    print(f"L to gal: {converter.convert(test_value, 'L', 'gal')}")
    test_value_m3 = 2.0
    print(f"\nTesting conversions for {test_value_m3} m3:")
    print(f"m3 to L: {converter.convert(test_value_m3, 'm3', 'L')}")
    print(f"m3 to gal: {converter.convert(test_value_m3, 'm3', 'gal')}")
    print(f"\nTesting same unit conversion:")
    print(f"L to L: {converter.convert(10, 'L', 'L')}")
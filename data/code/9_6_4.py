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
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    converter = VolumeConverter()
    test_value = 5.0
    print(f"Testing conversion for {test_value} L to ml:")
    result_ml = converter.convert(test_value, "L", "ml")
    print(f"{test_value} L = {result_ml} ml")
    print(f"\nTesting conversion for 2.0 m3 to L:")
    result_L = converter.convert(2.0, "m3", "L")
    print(f"2.0 m3 = {result_L} L")
    print(f"\nTesting conversion for 1.0 m3 to gal:")
    result_gal = converter.convert(1.0, "m3", "gal")
    print(f"1.0 m3 = {result_gal} gal")
    print(f"\nTesting conversion for 10.0 L to gal:")
    result_gal_2 = converter.convert(10.0, "L", "gal")
    print(f"10.0 L = {result_gal_2} gal")
    try:
        converter.convert(1.0, "m3", "ml")
    except ValueError as e:
        print(f"\nError caught: {e}")
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
            factor = self.conversion_factors["L_to_ml"]
            return value * factor
        if from_unit == "m3" and to_unit == "L":
            factor = self.conversion_factors["m3_to_L"]
            return value * factor
        if from_unit == "m3" and to_unit == "gal":
            factor = self.conversion_factors["m3_to_gal"]
            return value * factor
        if from_unit == "L" and to_unit == "gal":
            factor = self.conversion_factors["L_to_gal"]
            return value * factor
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    converter = VolumeConverter()
    print("--- Testing Conversions ---")
    value1 = 5.0
    from_unit1 = "L"
    to_unit1 = "ml"
    result1 = converter.convert(value1, from_unit1, to_unit1)
    print(f"{value1} {from_unit1} = {result1} {to_unit1}")
    value2 = 2.5
    from_unit2 = "m3"
    to_unit2 = "L"
    result2 = converter.convert(value2, from_unit2, to_unit2)
    print(f"{value2} {from_unit2} = {result2} {to_unit2}")
    value3 = 1.0
    from_unit3 = "m3"
    to_unit3 = "gal"
    result3 = converter.convert(value3, from_unit3, to_unit3)
    print(f"{value3} {from_unit3} = {result3} {to_unit3}")
    value4 = 10.0
    from_unit4 = "L"
    to_unit4 = "gal"
    result4 = converter.convert(value4, from_unit4, to_unit4)
    print(f"{value4} {from_unit4} = {result4} {to_unit4}")
    value5 = 100.0
    from_unit5 = "L"
    to_unit5 = "L"
    result5 = converter.convert(value5, from_unit5, to_unit5)
    print(f"{value5} {from_unit5} = {result5} {to_unit5}")
    try:
        converter.convert(1.0, "m3", "ml")
    except ValueError as e:
        print(f"Error caught: {e}")
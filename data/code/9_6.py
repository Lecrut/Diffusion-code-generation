class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            "L_to_ml": 1000.0,
            "m3_to_L": 1000.0,
            "L_to_gal": 0.264172,
            "m3_to_gal": 264.172,
            "ml_to_L": 0.001,
            "gal_to_L": 3.78541
        }
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "L" and to_unit == "ml":
            factor = self.conversion_factors["L_to_ml"]
            return value * factor
        elif from_unit == "ml" and to_unit == "L":
            factor = self.conversion_factors["ml_to_L"]
            return value * factor
        elif from_unit == "m3" and to_unit == "L":
            factor = self.conversion_factors["m3_to_L"]
            return value * factor
        elif from_unit == "L" and to_unit == "gal":
            factor = self.conversion_factors["L_to_gal"]
            return value * factor
        elif from_unit == "gal" and to_unit == "L":
            factor = self.conversion_factors["gal_to_L"]
            return value * factor
        elif from_unit == "L" and to_unit == "m3":
            factor = 1.0 / self.conversion_factors["m3_to_L"]
            return value / self.conversion_factors["m3_to_L"]
        elif from_unit == "m3" and to_unit == "L":
            factor = self.conversion_factors["m3_to_L"]
            return value * factor
        elif from_unit == "L" and to_unit == "m3":
            factor = 1.0 / self.conversion_factors["m3_to_L"]
            return value / self.conversion_factors["m3_to_L"]
        elif from_unit == "gal" and to_unit == "m3":
            factor = 1.0 / self.conversion_factors["m3_to_gal"]
            return value / self.conversion_factors["m3_to_gal"]
        elif from_unit == "m3" and to_unit == "gal":
            factor = self.conversion_factors["m3_to_gal"]
            return value * factor
        else:
            raise ValueError("Unsupported conversion pair")
if __name__ == '__main__':
    converter = VolumeConverter()
    print("--- Testing L to ml ---")
    liters = 5.0
    ml = converter.convert(liters, "L", "ml")
    print(f"{liters} L is {ml} ml")
    print("\n--- Testing ml to L ---")
    ml_val = 2500.0
    liters = converter.convert(ml_val, "ml", "L")
    print(f"{ml_val} ml is {liters} L")
    print("\n--- Testing L to gal ---")
    liters_val = 10.0
    gallons = converter.convert(liters_val, "L", "gal")
    print(f"{liters_val} L is {gallons} gal")
    print("\n--- Testing m3 to gal ---")
    m3_val = 1.0
    gallons_m3 = converter.convert(m3_val, "m3", "gal")
    print(f"{m3_val} m3 is {gallons_m3} gal")
    print("\n--- Testing m3 to L ---")
    m3_val_2 = 2.5
    liters_m3 = converter.convert(m3_val_2, "m3", "L")
    print(f"{m3_val_2} m3 is {liters_m3} L")
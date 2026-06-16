class UnitConverter:
    def convert_length(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "m":
            if to_unit == "cm":
                return value * 100
            elif to_unit == "km":
                return value / 1000
        elif from_unit == "cm":
            if to_unit == "m":
                return value / 100
        elif from_unit == "km":
            if to_unit == "m":
                return value * 1000
        return None
    def convert_mass(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "kg":
            if to_unit == "g":
                return value * 1000
            elif to_unit == "mg":
                return value * 1000000
        elif from_unit == "g":
            if to_unit == "kg":
                return value / 1000
        return None
    def convert_volume(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "L":
            if to_unit == "mL":
                return value * 1000
        elif from_unit == "mL":
            if to_unit == "L":
                return value / 1000
        return None
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion ---")
    length_val = 5
    from_l = "m"
    to_l = "cm"
    result_l = converter.convert_length(length_val, from_l, to_l)
    print(f"{length_val} {from_l} is {result_l} {to_l}")
    length_val = 2.5
    from_l = "km"
    to_l = "m"
    result_l = converter.convert_length(length_val, from_l, to_l)
    print(f"{length_val} {from_l} is {result_l} {to_l}")
    print("\n--- Mass Conversion ---")
    mass_val = 10
    from_m = "kg"
    to_m = "g"
    result_m = converter.convert_mass(mass_val, from_m, to_m)
    print(f"{mass_val} {from_m} is {result_m} {to_m}")
    mass_val = 500
    from_m = "g"
    to_m = "kg"
    result_m = converter.convert_mass(mass_val, from_m, to_m)
    print(f"{mass_val} {from_m} is {result_m} {to_m}")
    print("\n--- Volume Conversion ---")
    volume_val = 2
    from_v = "L"
    to_v = "mL"
    result_v = converter.convert_volume(volume_val, from_v, to_v)
    print(f"{volume_val} {from_v} is {result_v} {to_v}")
    volume_val = 500
    from_v = "mL"
    to_v = "L"
    result_v = converter.convert_volume(volume_val, from_v, to_v)
    print(f"{volume_val} {from_v} is {result_v} {to_v}")
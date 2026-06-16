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
    length_value = 5
    length_from = "m"
    length_to = "cm"
    length_result = converter.convert_length(length_value, length_from, length_to)
    print(f"Length Conversion: {length_value} {length_from} = {length_result} {length_to}")
    length_value = 2.5
    length_from = "km"
    length_to = "m"
    length_result = converter.convert_length(length_value, length_from, length_to)
    print(f"Length Conversion: {length_value} {length_from} = {length_result} {length_to}")
    mass_value = 10
    mass_from = "kg"
    mass_to = "g"
    mass_result = converter.convert_mass(mass_value, mass_from, mass_to)
    print(f"Mass Conversion: {mass_value} {mass_from} = {mass_result} {mass_to}")
    mass_value = 500
    mass_from = "g"
    mass_to = "kg"
    mass_result = converter.convert_mass(mass_value, mass_from, mass_to)
    print(f"Mass Conversion: {mass_value} {mass_from} = {mass_result} {mass_to}")
    volume_value = 2
    volume_from = "L"
    volume_to = "mL"
    volume_result = converter.convert_volume(volume_value, volume_from, volume_to)
    print(f"Volume Conversion: {volume_value} {volume_from} = {volume_result} {volume_to}")
    volume_value = 500
    volume_from = "mL"
    volume_to = "L"
    volume_result = converter.convert_volume(volume_value, volume_from, volume_to)
    print(f"Volume Conversion: {volume_value} {volume_from} = {volume_result} {volume_to}")
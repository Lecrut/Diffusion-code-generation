class UnitConverter:
    @staticmethod
    def convert_mass(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'kg' and to_unit == 'lb':
            return value * 2.2046226218
        elif from_unit == 'lb' and to_unit == 'kg':
            return value / 2.2046226218
        return None
    @staticmethod
    def convert_length(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'm' and to_unit == 'ft':
            return value * 3.28084
        elif from_unit == 'ft' and to_unit == 'm':
            return value / 3.28084
        return None
if __name__ == '__main__':
    mass_kg = 10
    mass_lb = UnitConverter.convert_mass(mass_kg, 'kg', 'lb')
    print(f"{mass_kg} kg is {mass_lb:.2f} lb")
    mass_back = UnitConverter.convert_mass(mass_lb, 'lb', 'kg')
    print(f"{mass_lb:.2f} lb is {mass_back:.2f} kg")
    length_m = 10
    length_ft = UnitConverter.convert_length(length_m, 'm', 'ft')
    print(f"{length_m} m is {length_ft:.2f} ft")
    length_back = UnitConverter.convert_length(length_ft, 'ft', 'm')
    print(f"{length_ft:.2f} ft is {length_back:.2f} m")
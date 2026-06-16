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
    print(f"{mass_kg} kg is equal to {mass_lb:.2f} lb")
    mass_lb_to_kg = 150
    mass_kg_from_lb = UnitConverter.convert_mass(mass_lb_to_kg, 'lb', 'kg')
    print(f"{mass_lb_to_kg} lb is equal to {mass_kg_from_lb:.2f} kg")
    length_m = 10
    length_ft = UnitConverter.convert_length(length_m, 'm', 'ft')
    print(f"{length_m} m is equal to {length_ft:.2f} ft")
    length_ft_to_m = 6.5
    length_m_from_ft = UnitConverter.convert_length(length_ft_to_m, 'ft', 'm')
    print(f"{length_ft_to_m} ft is equal to {length_m_from_ft:.2f} m")
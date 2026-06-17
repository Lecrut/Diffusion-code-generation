class MassConverter:
    def convert_mass(self, mass, from_unit, to_unit):
        if from_unit == to_unit:
            return mass
        if from_unit == 'kg':
            if to_unit == 'g':
                return mass * 1000
            elif to_unit == 'lb':
                return mass * 2.20462
        elif from_unit == 'g':
            if to_unit == 'kg':
                return mass / 1000
            elif to_unit == 'lb':
                return mass * 0.00220462
        elif from_unit == 'lb':
            if to_unit == 'kg':
                return mass / 2.20462
            elif to_unit == 'g':
                return mass * 1000
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    converter = MassConverter()
    mass_kg = 5
    from_unit = 'kg'
    to_unit = 'g'
    result1 = converter.convert_mass(mass_kg, from_unit, to_unit)
    print(f"{mass_kg} {from_unit} is {result1} {to_unit}")
    mass_g = 5000
    from_unit = 'g'
    to_unit = 'kg'
    result2 = converter.convert_mass(mass_g, from_unit, to_unit)
    print(f"{mass_g} {from_unit} is {result2} {to_unit}")
    mass_lb = 10
    from_unit = 'lb'
    to_unit = 'kg'
    result3 = converter.convert_mass(mass_lb, from_unit, to_unit)
    print(f"{mass_lb} {from_unit} is {result3} {to_unit}")
    mass_kg_2 = 10
    from_unit = 'kg'
    to_unit = 'lb'
    result4 = converter.convert_mass(mass_kg_2, from_unit, to_unit)
    print(f"{mass_kg_2} {from_unit} is {result4} {to_unit}")
    mass_same = 100
    from_unit = 'kg'
    to_unit = 'kg'
    result5 = converter.convert_mass(mass_same, from_unit, to_unit)
    print(f"{mass_same} {from_unit} is {result5} {to_unit}")
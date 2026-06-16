class MassConverter:
    def convert(self, mass, from_unit, to_unit):
        if from_unit == to_unit:
            return mass
        if from_unit == 'kg':
            if to_unit == 'g':
                return mass * 1000
            elif to_unit == 'lb':
                return mass * 2.2046226218
        elif from_unit == 'g':
            if to_unit == 'kg':
                return mass / 1000
            elif to_unit == 'lb':
                return mass * 0.0022046226218
        elif from_unit == 'lb':
            if to_unit == 'kg':
                return mass / 2.2046226218
            elif to_unit == 'g':
                return mass * 1000
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    converter = MassConverter()
    mass_kg = 5.0
    from_unit = 'kg'
    to_unit = 'g'
    result1 = converter.convert(mass_kg, from_unit, to_unit)
    print(f"{mass_kg} kg is {result1} g")
    mass_g = 5000.0
    from_unit = 'g'
    to_unit = 'kg'
    result2 = converter.convert(mass_g, from_unit, to_unit)
    print(f"{mass_g} g is {result2} kg")
    mass_lb = 10.0
    from_unit = 'lb'
    to_unit = 'kg'
    result3 = converter.convert(mass_lb, from_unit, to_unit)
    print(f"{mass_lb} lb is {result3} kg")
    mass_kg_2 = 1.0
    from_unit = 'kg'
    to_unit = 'lb'
    result4 = converter.convert(mass_kg_2, from_unit, to_unit)
    print(f"{mass_kg_2} kg is {result4} lb")
    mass_same = 100.0
    from_unit = 'g'
    to_unit = 'g'
    result5 = converter.convert(mass_same, from_unit, to_unit)
    print(f"{mass_same} g is {result5} g")
    mass_g_2 = 1000.0
    from_unit = 'g'
    to_unit = 'lb'
    result6 = converter.convert(mass_g_2, from_unit, to_unit)
    print(f"{mass_g_2} g is {result6} lb")
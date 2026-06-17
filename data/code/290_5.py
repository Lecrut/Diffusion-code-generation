class MassConverter:
    def convert(self, mass, from_unit, to_unit):
        if from_unit == to_unit:
            return mass
        mass_in_kg = 0.0
        if from_unit == "kg":
            mass_in_kg = mass
        elif from_unit == "g":
            mass_in_kg = mass / 1000.0
        elif from_unit == "lb":
            mass_in_kg = mass * 0.453592
        else:
            raise ValueError("Unsupported 'from_unit'")
        if to_unit == "kg":
            return mass_in_kg
        elif to_unit == "g":
            return mass_in_kg * 1000.0
        elif to_unit == "lb":
            return mass_in_kg / 0.453592
        else:
            raise ValueError("Unsupported 'to_unit'")
if __name__ == '__main__':
    converter = MassConverter()
    mass1 = 5.0
    from_unit1 = "kg"
    to_unit1 = "g"
    result1 = converter.convert(mass1, from_unit1, to_unit1)
    print(f"{mass1} {from_unit1} is {result1} {to_unit1}")
    mass2 = 150.0
    from_unit2 = "lb"
    to_unit2 = "kg"
    result2 = converter.convert(mass2, from_unit2, to_unit2)
    print(f"{mass2} {from_unit2} is {result2} {to_unit2}")
    mass3 = 2000.0
    from_unit3 = "g"
    to_unit3 = "lb"
    result3 = converter.convert(mass3, from_unit3, to_unit3)
    print(f"{mass3} {from_unit3} is {result3} {to_unit3}")
    mass4 = 10.0
    from_unit4 = "kg"
    to_unit4 = "kg"
    result4 = converter.convert(mass4, from_unit4, to_unit4)
    print(f"{mass4} {from_unit4} is {result4} {to_unit4}")
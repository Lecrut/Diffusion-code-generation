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
            raise ValueError("Unsupported 'from_unit'. Supported units are kg, g, lb.")
        if to_unit == "kg":
            return mass_in_kg
        elif to_unit == "g":
            return mass_in_kg * 1000.0
        elif to_unit == "lb":
            return mass_in_kg / 0.453592
        else:
            raise ValueError("Unsupported 'to_unit'. Supported units are kg, g, lb.")
if __name__ == '__main__':
    converter = MassConverter()
    mass1 = 5.0
    from_unit1 = "kg"
    to_unit1 = "g"
    result1 = converter.convert(mass1, from_unit1, to_unit1)
    print(f"{mass1} {from_unit1} is {result1} {to_unit1}")
    mass2 = 2500.0
    from_unit2 = "g"
    to_unit2 = "kg"
    result2 = converter.convert(mass2, from_unit2, to_unit2)
    print(f"{mass2} {from_unit2} is {result2} {to_unit2}")
    mass3 = 150.0
    from_unit3 = "lb"
    to_unit3 = "kg"
    result3 = converter.convert(mass3, from_unit3, to_unit3)
    print(f"{mass3} {from_unit3} is {result3} {to_unit3}")
    mass4 = 10.0
    from_unit4 = "kg"
    to_unit4 = "lb"
    result4 = converter.convert(mass4, from_unit4, to_unit4)
    print(f"{mass4} {from_unit4} is {result4} {to_unit4}")
    mass5 = 1000.0
    from_unit5 = "g"
    to_unit5 = "lb"
    result5 = converter.convert(mass5, from_unit5, to_unit5)
    print(f"{mass5} {from_unit5} is {result5} {to_unit5}")
    mass6 = 10.0
    from_unit6 = "kg"
    to_unit6 = "kg"
    result6 = converter.convert(mass6, from_unit6, to_unit6)
    print(f"{mass6} {from_unit6} is {result6} {to_unit6}")
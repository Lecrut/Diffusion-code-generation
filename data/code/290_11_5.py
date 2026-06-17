class MassConverter:
    def to_grams(self, mass_kg):
        return mass_kg * 1000
    def to_pounds(self, mass_kg):
        return mass_kg * 2.20462
    def to_kilograms(self, mass_g):
        return mass_g / 1000
    def to_pounds_from_pounds(self, mass_lb):
        return mass_lb
    def to_grams_from_grams(self, mass_g):
        return mass_g
if __name__ == '__main__':
    converter = MassConverter()
    mass_kg = 5.0
    print(f"Converting {mass_kg} kg:")
    print(f"To grams: {converter.to_grams(mass_kg)}")
    print(f"To pounds: {converter.to_pounds(mass_kg)}")
    mass_g = 1500.0
    print(f"\nConverting {mass_g} g:")
    print(f"To kilograms: {converter.to_kilograms(mass_g)}")
    mass_lb = 10.0
    print(f"\nConverting {mass_lb} lb:")
    print(f"To pounds (identity): {converter.to_pounds_from_pounds(mass_lb)}")
    mass_kg_2 = 2.5
    print(f"\nConverting {mass_kg_2} kg to grams: {converter.to_grams(mass_kg_2)}")
    print(f"Converting {mass_kg_2} kg to pounds: {converter.to_pounds(mass_kg_2)}")
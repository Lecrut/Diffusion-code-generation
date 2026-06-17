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
    mass_lb = 10.0
    print(f"\nConverting {mass_lb} lbs:")
    print(f"To kilograms: {converter.to_kilograms(mass_lb)}")
    mass_g = 500.0
    print(f"\nConverting {mass_g} g:")
    print(f"To kilograms: {converter.to_kilograms(mass_g)}")
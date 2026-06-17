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
    mass_kg_sample = 5.5
    mass_lb_sample = 10.0
    print(f"Converting {mass_kg_sample} kg:")
    grams = converter.to_grams(mass_kg_sample)
    pounds = converter.to_pounds(mass_kg_sample)
    print(f"{mass_kg_sample} kg is equal to {grams} grams")
    print(f"{mass_kg_sample} kg is equal to {pounds} pounds")
    print("\nConverting from Grams:")
    grams_sample = 2500.0
    kg_from_g = converter.to_kilograms(grams_sample)
    print(f"{grams_sample} grams is equal to {kg_from_g} kg")
    print("\nConverting from Pounds:")
    pounds_sample = 15.0
    kg_from_lb = converter.to_kilograms(pounds_sample * 2.20462)
    print(f"{pounds_sample} pounds is equal to {kg_from_lb} kg")
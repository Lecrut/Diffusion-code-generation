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
    print("\nConverting {mass_lb_sample} lbs:")
    kg_from_lb = converter.to_kilograms(mass_lb_sample * 2.20462)
    print(f"{mass_lb_sample} lbs is equal to {kg_from_lb:.4f} kg")
    print("\nDirect conversion check:")
    grams_check = converter.to_grams(1000)
    kg_check = converter.to_kilograms(grams_check)
    print(f"1000 grams converted back to kg: {kg_check}")
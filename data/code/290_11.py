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
    print(f"Converting {mass_kg_sample} kg:")
    print(f"To grams: {converter.to_grams(mass_kg_sample)}")
    print(f"To pounds: {converter.to_pounds(mass_kg_sample)}")
    mass_g_sample = 1500
    print(f"\nConverting {mass_g_sample} g:")
    print(f"To kilograms: {converter.to_kilograms(mass_g_sample)}")
    mass_lb_sample = 10.0
    print(f"\nConverting {mass_lb_sample} lb:")
    print(f"To kilograms (via direct conversion): {converter.to_kilograms(mass_lb_sample * 2.20462)}")
    print(f"\nDirect pound to pound check: {converter.to_pounds_from_pounds(10.0)} lb")
    print(f"Direct gram to gram check: {converter.to_grams_from_grams(1500)} g")
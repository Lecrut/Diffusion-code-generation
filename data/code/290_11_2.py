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
    kg_value = 5.5
    print(f"Converting {kg_value} kg:")
    print(f"To grams: {converter.to_grams(kg_value)}")
    print(f"To pounds: {converter.to_pounds(kg_value)}")
    g_value = 1500
    print(f"\nConverting {g_value} g:")
    print(f"To kilograms: {converter.to_kilograms(g_value)}")
    lb_value = 10.0
    print(f"\nConverting {lb_value} lbs:")
    print(f"To kilograms (via direct conversion): {converter.to_pounds_from_pounds(lb_value) / 2.20462}")
class MassConverter:
    def __init__(self):
        self.kg_to_lb = 2.20462
        self.g_to_oz = 0.035274
    def kg_to_pounds(self, kilograms):
        return kilograms * self.kg_to_lb
    def g_to_ounces(self, grams):
        return grams * self.g_to_oz
if __name__ == '__main__':
    converter = MassConverter()
    sample_kg = 50.0
    sample_g = 128.0
    pounds_value = converter.kg_to_pounds(sample_kg)
    ounces_value = converter.g_to_ounces(sample_g)
    print(f"{sample_kg} kg equals {pounds_value:.4f} lbs")
    print(f"{sample_g} g equals {ounces_value:.4f} oz")
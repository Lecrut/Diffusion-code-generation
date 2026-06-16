class MassConverter:
    def __init__(self):
        self.base_unit = "kg"
        self.conversion_factors = {
            "kg": 1.0,
            "g": 0.001,
            "mg": 0.000001,
            "lb": 0.453592,
            "oz": 0.0283495
        }
    def convert(self, mass: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("Unsupported unit provided.")
        mass_in_base = mass * self.conversion_factors[from_unit]
        result = mass_in_base / self.conversion_factors[to_unit]
        return result
if __name__ == '__main__':
    converter = MassConverter()
    mass_kg = 10.0
    mass_g = 500.0
    mass_lb = 2.20462                                 
    print(f"{mass_kg} kg is {converter.convert(mass_kg, 'kg', 'g'):.2f} g")
    print(f"{mass_g} g is {converter.convert(mass_g, 'g', 'kg'):.2f} kg")
    print(f"{mass_lb} lb is {converter.convert(mass_lb, 'lb', 'kg'):.4f} kg")
    print(f"1000 g is {converter.convert(1000.0, 'g', 'kg'):.3f} kg")
    print(f"10 lb is {converter.convert(10.0, 'lb', 'oz'):.2f} oz")
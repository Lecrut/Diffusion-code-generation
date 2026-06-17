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
    from_unit = "kg"
    to_unit = "g"
    result1 = converter.convert(mass_kg, from_unit, to_unit)
    print(f"{mass_kg} {from_unit} is equal to {result1:.6f} {to_unit}")
    mass_lb = 2.20462
    from_unit = "lb"
    to_unit = "kg"
    result2 = converter.convert(mass_lb, from_unit, to_unit)
    print(f"{mass_lb} {from_unit} is equal to {result2:.6f} {to_unit}")
    mass_mg = 5000.0
    from_unit = "mg"
    to_unit = "g"
    result3 = converter.convert(mass_mg, from_unit, to_unit)
    print(f"{mass_mg} {from_unit} is equal to {result3:.6f} {to_unit}")
    mass_oz = 100.0
    from_unit = "oz"
    to_unit = "lb"
    result4 = converter.convert(mass_oz, from_unit, to_unit)
    print(f"{mass_oz} {from_unit} is equal to {result4:.6f} {to_unit}")
class MassConverter:
    def __init__(self):
        self.base_unit = "kg"
        self.conversion_factors = {
            "kg": 1.0,
            "g": 0.001,
            "mg": 0.000001,
            "lb": 0.453592,
            "oz": 0.0283495,
        }
    def convert(self, mass: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("Unsupported unit provided.")
        mass_in_base = mass * self.conversion_factors[from_unit]
        result = mass_in_base / self.conversion_factors[to_unit]
        return result
if __name__ == '__main__':
    converter = MassConverter()
    mass1 = 10.0
    from_unit1 = "kg"
    to_unit1 = "g"
    result1 = converter.convert(mass1, from_unit1, to_unit1)
    print(f"{mass1} {from_unit1} is equal to {result1} {to_unit1}")
    mass2 = 2.0
    from_unit2 = "lb"
    to_unit2 = "kg"
    result2 = converter.convert(mass2, from_unit2, to_unit2)
    print(f"{mass2} {from_unit2} is equal to {result2} {to_unit2}")
    mass3 = 5000.0
    from_unit3 = "mg"
    to_unit3 = "g"
    result3 = converter.convert(mass3, from_unit3, to_unit3)
    print(f"{mass3} {from_unit3} is equal to {result3} {to_unit3}")
    mass4 = 10.0
    from_unit4 = "oz"
    to_unit4 = "lb"
    result4 = converter.convert(mass4, from_unit4, to_unit4)
    print(f"{mass4} {from_unit4} is equal to {result4} {to_unit4}")
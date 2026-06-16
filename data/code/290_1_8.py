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
            raise ValueError("Invalid unit specified.")
        if from_unit == to_unit:
            return mass
        mass_in_base = mass * self.conversion_factors[from_unit]
        result = mass_in_base / self.conversion_factors[to_unit]
        return result
if __name__ == '__main__':
    converter = MassConverter()
    mass_kg = 5.0
    from_unit_1 = "kg"
    to_unit_1 = "g"
    result_1 = converter.convert(mass_kg, from_unit_1, to_unit_1)
    print(f"{mass_kg} {from_unit_1} is equal to {result_1} {to_unit_1}")
    mass_lb = 150.0
    from_unit_2 = "lb"
    to_unit_2 = "kg"
    result_2 = converter.convert(mass_lb, from_unit_2, to_unit_2)
    print(f"{mass_lb} {from_unit_2} is equal to {result_2} {to_unit_2}")
    mass_mg = 5000.0
    from_unit_3 = "mg"
    to_unit_3 = "oz"
    result_3 = converter.convert(mass_mg, from_unit_3, to_unit_3)
    print(f"{mass_mg} {from_unit_3} is equal to {result_3} {to_unit_3}")
    mass_same = 10.0
    from_unit_4 = "kg"
    to_unit_4 = "kg"
    result_4 = converter.convert(mass_same, from_unit_4, to_unit_4)
    print(f"{mass_same} {from_unit_4} is equal to {result_4} {to_unit_4}")
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
    def convert(self, mass, unit):
        if unit == 'kg':
            if mass_unit == 'g':
                return self.to_grams(mass)
            elif mass_unit == 'lb':
                return self.to_pounds(mass)
            else:
                raise ValueError("Invalid target unit for kg conversion")
        elif unit == 'g':
            if mass_unit == 'kg':
                return self.to_kilograms(mass)
            elif mass_unit == 'lb':
                return self.to_pounds(self.to_grams(mass))
            else:
                raise ValueError("Invalid target unit for g conversion")
        else:
            raise ValueError("Invalid input unit specified")
if __name__ == '__main__':
    converter = MassConverter()
    kg_value = 5.0
    lb_value = 10.0
    print(f"Converting {kg_value} kg:")
    grams = converter.to_grams(kg_value)
    pounds = converter.to_pounds(kg_value)
    print(f"{kg_value} kg is equal to {grams} grams")
    print(f"{kg_value} kg is equal to {pounds} pounds")
    print("\nConverting {lb_value} lb:")
    kg_from_lb = converter.to_kilograms(lb_value / 2.20462)                                                                                                                              
    pounds_result = converter.to_pounds_from_pounds(lb_value)
    print(f"{lb_value} lb is equal to {pounds_result} pounds (identity check)")
    kg_test = 10.5
    grams_result = converter.to_grams(kg_test)
    kg_roundtrip = converter.to_kilograms(grams_result)
    print(f"\nRound trip test: {kg_test} kg -> {grams_result} g -> {kg_roundtrip} kg")
    lb_test = 2.20462
    grams_from_lb = converter.to_grams(lb_test)
    pounds_from_g = converter.to_pounds(grams_from_lb)
    print(f"Round trip test: {lb_test} lb -> {grams_from_lb} g -> {pounds_from_g} lb")
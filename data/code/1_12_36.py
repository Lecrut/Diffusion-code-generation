class WeightConverter:
    def __init__(self):
        self.kg_to_pounds_factor = 2.20462

    def kg_to_pounds(self, kg):
        return kg * self.kg_to_pounds_factor

    def pounds_to_kg(self, pounds):
        return pounds / self.kg_to_pounds_factor

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg = 80
    sample_pounds = 176
    converted_pounds = converter.kg_to_pounds(sample_kg)
    converted_kg = converter.pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
class WeightConverter:
    def __init__(self):
        self.factor = 2.20462

    def convert_kg_to_pounds(self, kg):
        return kg * self.factor

    def convert_pounds_to_kg(self, pounds):
        return pounds / self.factor

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg = 90
    sample_pounds = 198
    converted_pounds = converter.convert_kg_to_pounds(sample_kg)
    converted_kg = converter.convert_pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
class WeightConverter:
    def __init__(self):
        self.CONVERSION_FACTOR = 2.20462

    def kg_to_pounds(self, kg):
        return kg * self.CONVERSION_FACTOR

    def pounds_to_kg(self, pounds):
        return pounds / self.CONVERSION_FACTOR

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg_1 = 90
    sample_pounds_1 = 200
    converted_pounds_1 = converter.kg_to_pounds(sample_kg_1)
    converted_kg_1 = converter.pounds_to_kg(sample_pounds_1)

    sample_kg_2 = 60
    sample_pounds_2 = 132
    converted_pounds_2 = converter.kg_to_pounds(sample_kg_2)
    converted_kg_2 = converter.pounds_to_kg(sample_pounds_2)

    print(f"{sample_kg_1} kg is {converted_pounds_1:.2f} pounds")
    print(f"{sample_pounds_1} pounds is {converted_kg_1:.2f} kg")
    print(f"{sample_kg_2} kg is {converted_pounds_2:.2f} pounds")
    print(f"{sample_pounds_2} pounds is {converted_kg_2:.2f} kg")
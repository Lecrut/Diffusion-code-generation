class WeightConverter:
    def __init__(self):
        self._factor = 2.20462

    def kg_to_pounds(self, kg):
        return kg * self._factor

    def pounds_to_kg(self, pounds):
        return pounds / self._factor

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg1 = 70
    sample_kg2 = 90
    sample_pounds1 = 154
    sample_pounds2 = 198

    converted_pounds1 = converter.kg_to_pounds(sample_kg1)
    converted_kg1 = converter.pounds_to_kg(sample_pounds1)
    converted_pounds2 = converter.kg_to_pounds(sample_kg2)
    converted_kg2 = converter.pounds_to_kg(sample_pounds2)

    print(f"{sample_kg1} kg is {converted_pounds1:.2f} pounds")
    print(f"{sample_pounds1} pounds is {converted_kg1:.2f} kg")
    print(f"{sample_kg2} kg is {converted_pounds2:.2f} pounds")
    print(f"{sample_pounds2} pounds is {converted_kg2:.2f} kg")
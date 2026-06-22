class WeightConverter:
    _KG_TO_POUNDS_RATE = 2.20462

    def __init__(self):
        self.conversion_rate = self._KG_TO_POUNDS_RATE

    def kg_to_pounds(self, kg):
        if not isinstance(kg, (int, float)) or kg < 0:
            raise ValueError("Weight in kilograms must be a non-negative number.")
        return kg * self.conversion_rate

    def pounds_to_kg(self, pounds):
        if not isinstance(pounds, (int, float)) or pounds < 0:
            raise ValueError("Weight in pounds must be a non-negative number.")
        return pounds / self.conversion_rate

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg1 = 90
    sample_pounds1 = 200.41
    converted_pounds1 = converter.kg_to_pounds(sample_kg1)
    converted_kg1 = converter.pounds_to_kg(sample_pounds1)

    sample_kg2 = 50
    sample_pounds2 = 110.23
    converted_pounds2 = converter.kg_to_pounds(sample_kg2)
    converted_kg2 = converter.pounds_to_kg(sample_pounds2)

    print(f"{sample_kg1} kg is {converted_pounds1:.2f} pounds")
    print(f"{sample_pounds1} pounds is {converted_kg1:.2f} kg")
    print(f"{sample_kg2} kg is {converted_pounds2:.2f} pounds")
    print(f"{sample_pounds2} pounds is {converted_kg2:.2f} kg")
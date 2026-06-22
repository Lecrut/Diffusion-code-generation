class WeightConverter:
    _KG_TO_POUNDS_RATE = 2.20462

    def kg_to_pounds(self, kg):
        if not isinstance(kg, (int, float)) or kg < 0:
            raise ValueError("Weight in kilograms must be a non-negative number.")
        return kg * self._KG_TO_POUNDS_RATE

    def pounds_to_kg(self, pounds):
        if not isinstance(pounds, (int, float)) or pounds < 0:
            raise ValueError("Weight in pounds must be a non-negative number.")
        return pounds / self._KG_TO_POUNDS_RATE

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg = 68
    sample_pounds = 150.26
    converted_pounds = converter.kg_to_pounds(sample_kg)
    converted_kg = converter.pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
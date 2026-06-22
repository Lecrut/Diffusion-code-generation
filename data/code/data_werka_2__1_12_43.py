class WeightConverter:
    def __init__(self):
        self.CONVERSION_FACTOR = 2.20462

    def _validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number")
        if value < 0:
            raise ValueError("Weight cannot be negative")

    def kg_to_pounds(self, kg):
        self._validate_input(kg)
        return kg * self.CONVERSION_FACTOR

    def pounds_to_kg(self, pounds):
        self._validate_input(pounds)
        return pounds / self.CONVERSION_FACTOR

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg = 90
    sample_pounds = 198
    converted_pounds = converter.kg_to_pounds(sample_kg)
    converted_kg = converter.pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
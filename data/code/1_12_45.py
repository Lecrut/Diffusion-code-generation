class WeightConverter:
    def __init__(self):
        self.CONVERSION_FACTOR = 2.20462

    def kg_to_pounds(self, kg):
        if kg < 0:
            raise ValueError("Weight in kilograms cannot be negative.")
        return kg * self.CONVERSION_FACTOR

    def pounds_to_kg(self, pounds):
        if pounds < 0:
            raise ValueError("Weight in pounds cannot be negative.")
        return pounds / self.CONVERSION_FACTOR

if __name__ == '__main__':
    converter = WeightConverter()
    sample_kg = 90
    sample_pounds = 198
    try:
        converted_to_pounds = converter.kg_to_pounds(sample_kg)
        converted_to_kg = converter.pounds_to_kg(sample_pounds)
        print(f"{sample_kg} kg is {converted_to_pounds:.2f} pounds")
        print(f"{sample_pounds} pounds is {converted_to_kg:.2f} kg")
    except ValueError as e:
        print(e)
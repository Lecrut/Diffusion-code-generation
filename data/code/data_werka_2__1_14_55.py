class WeightConverter:
    _CONVERSION_RATE = 2.20462

    @staticmethod
    def _validate_weight(weight):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Weight must be a non-negative number.")

    @classmethod
    def kg_to_pounds(cls, kg):
        cls._validate_weight(kg)
        return kg * cls._CONVERSION_RATE

    @classmethod
    def pounds_to_kg(cls, pounds):
        cls._validate_weight(pounds)
        return pounds / cls._CONVERSION_RATE

if __name__ == '__main__':
    sample_kg = 72
    sample_pounds = 158.73

    converted_pounds = WeightConverter.kg_to_pounds(sample_kg)
    converted_kg = WeightConverter.pounds_to_kg(sample_pounds)

    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
class WeightConverter:
    _CONVERSION_RATE = 2.20462

    @staticmethod
    def validate_weight(weight):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Weight must be a non-negative number.")

    @classmethod
    def kg_to_pounds(cls, kg):
        cls.validate_weight(kg)
        return kg * cls._CONVERSION_RATE

    @classmethod
    def pounds_to_kg(cls, pounds):
        cls.validate_weight(pounds)
        return pounds / cls._CONVERSION_RATE

if __name__ == '__main__':
    sample_kg = 90
    sample_pounds = 198.43
    try:
        converted_pounds = WeightConverter.kg_to_pounds(sample_kg)
        print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
        converted_kg = WeightConverter.pounds_to_kg(sample_pounds)
        print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
    except ValueError as e:
        print(e)
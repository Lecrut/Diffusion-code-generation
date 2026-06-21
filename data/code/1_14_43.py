class WeightConverter:
    _CONVERSION_RATE = 2.20462

    @classmethod
    def kg_to_pounds(cls, kg):
        if not isinstance(kg, (int, float)) or kg < 0:
            raise ValueError("Weight in kilograms must be a non-negative number.")
        return kg * cls._CONVERSION_RATE

    @classmethod
    def pounds_to_kg(cls, pounds):
        if not isinstance(pounds, (int, float)) or pounds < 0:
            raise ValueError("Weight in pounds must be a non-negative number.")
        return pounds / cls._CONVERSION_RATE

if __name__ == '__main__':
    sample_kg = 80
    sample_pounds = 176.37
    try:
        converted_pounds = WeightConverter.kg_to_pounds(sample_kg)
        print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    except ValueError as e:
        print(e)

    try:
        converted_kg = WeightConverter.pounds_to_kg(sample_pounds)
        print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
    except ValueError as e:
        print(e)
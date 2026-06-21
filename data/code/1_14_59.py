class WeightConverter:
    KG_TO_POUNDS = 2.20462

    @staticmethod
    def convert_kg_to_pounds(kg):
        if kg < 0:
            raise ValueError("Weight in kilograms must be a non-negative number.")
        return kg * WeightConverter.KG_TO_POUNDS

    @staticmethod
    def convert_pounds_to_kg(pounds):
        if pounds < 0:
            raise ValueError("Weight in pounds must be a non-negative number.")
        return pounds / WeightConverter.KG_TO_POUNDS

if __name__ == '__main__':
    sample_kg = 90
    sample_pounds = 198.426
    converted_pounds = WeightConverter.convert_kg_to_pounds(sample_kg)
    converted_kg = WeightConverter.convert_pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
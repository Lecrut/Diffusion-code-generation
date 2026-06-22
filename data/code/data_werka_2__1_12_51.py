class WeightConverter:
    KG_TO_POUNDS_FACTOR = 2.20462

    @staticmethod
    def kg_to_pounds(kg):
        return kg * WeightConverter.KG_TO_POUNDS_FACTOR

    @staticmethod
    def pounds_to_kg(pounds):
        return pounds / WeightConverter.KG_TO_POUNDS_FACTOR

if __name__ == '__main__':
    sample_kg = 60
    sample_pounds = 132
    converted_pounds = WeightConverter.kg_to_pounds(sample_kg)
    converted_kg = WeightConverter.pounds_to_kg(sample_pounds)
    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
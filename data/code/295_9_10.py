class WeightConverter:
    CONVERSION_FACTOR = 2.20462

    @staticmethod
    def kg_to_lbs(kg):
        return kg * WeightConverter.CONVERSION_FACTOR

    @staticmethod
    def lbs_to_kg(lbs):
        return lbs / WeightConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    kilograms = 10
    pounds = 22.0462
    converted_pounds = WeightConverter.kg_to_lbs(kilograms)
    print(f"{kilograms} kg is equal to {converted_pounds:.2f} lbs")
    converted_kg = WeightConverter.lbs_to_kg(pounds)
    print(f"{pounds} lbs is equal to {converted_kg:.2f} kg")
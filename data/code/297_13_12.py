class WeightConverter:
    POUNDS_TO_KG_FACTOR = 0.45359237
    KG_TO_POUNDS_FACTOR = 1 / POUNDS_TO_KG_FACTOR

    @staticmethod
    def pounds_to_kg(pounds):
        return pounds * WeightConverter.POUNDS_TO_KG_FACTOR

    @staticmethod
    def kg_to_pounds(kg):
        return kg * WeightConverter.KG_TO_POUNDS_FACTOR
if __name__ == '__main__':
    print(WeightConverter.pounds_to_kg(10))
    print(WeightConverter.kg_to_pounds(5))
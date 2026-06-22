class WeightConverter:
    POUND_TO_KILOGRAM = 0.45359237
    KILOGRAM_TO_POUND = 1 / POUND_TO_KILOGRAM

    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds * WeightConverter.POUND_TO_KILOGRAM

    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms * WeightConverter.KILOGRAM_TO_POUND
if __name__ == '__main__':
    print(WeightConverter.pounds_to_kilograms(10))
    print(WeightConverter.kilograms_to_pounds(1))
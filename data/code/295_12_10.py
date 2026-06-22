class WeightConverter:
    CONVERSION_FACTOR = 0.453592

    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds * WeightConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    sample_pounds = 100.0
    kilograms_result = WeightConverter.pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is {kilograms_result:.2f} kg")
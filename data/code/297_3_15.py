class WeightConverter:
    ConversionFactor = 0.453592

    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds * WeightConverter.ConversionFactor

if __name__ == '__main__':
    sample_pounds = 10
    print(WeightConverter.pounds_to_kilograms(sample_pounds))
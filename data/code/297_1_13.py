class ConversionHelper:
    GALLONS_TO_LITERS = 3.78541

    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * ConversionHelper.GALLONS_TO_LITERS

if __name__ == '__main__':
    sample_gallons = 5.0
    result = ConversionHelper.gallons_to_liters(sample_gallons)
    print(result)
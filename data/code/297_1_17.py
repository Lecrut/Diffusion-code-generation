class UnitConverter:
    GALLON_TO_LITER_FACTOR = 3.78541

    @staticmethod
    def convert_gallons_to_liters(gallons):
        return gallons * UnitConverter.GALLON_TO_LITER_FACTOR

if __name__ == '__main__':
    sample_gallons = 5
    result_liters = UnitConverter.convert_gallons_to_liters(sample_gallons)
    print(result_liters)
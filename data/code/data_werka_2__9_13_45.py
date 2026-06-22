class UnitConverter:
    LITERS_PER_GALLON = 3.78541

    @staticmethod
    def convert_gallons_to_liters(gallons):
        if gallons < 0:
            raise ValueError("Gallons cannot be negative")
        return gallons * UnitConverter.LITERS_PER_GALLON

if __name__ == '__main__':
    sample_volume_gallons = 15.0
    converter = UnitConverter()
    converted_liters = converter.convert_gallons_to_liters(sample_volume_gallons)
    print(converted_liters)
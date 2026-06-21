class VolumeConverter:
    LITERS_PER_GALLON = 3.78541

    @staticmethod
    def gallons_to_liters(gallons):
        if gallons < 0:
            raise ValueError("Gallons cannot be negative")
        return gallons * VolumeConverter.LITERS_PER_GALLON

if __name__ == '__main__':
    sample_gallons = 7.5
    converter = VolumeConverter()
    converted_liters = converter.gallons_to_liters(sample_gallons)
    print(converted_liters)
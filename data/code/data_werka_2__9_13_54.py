class VolumeConverter:
    LITERS_PER_GALLON = 3.78541

    @staticmethod
    def convert_gallons_to_liters(gallons):
        if gallons < 0:
            raise ValueError("Gallons cannot be negative")
        return gallons * VolumeConverter.LITERS_PER_GALLON

if __name__ == '__main__':
    sample_volume_gallons = 2.5
    converted_liters = VolumeConverter.convert_gallons_to_liters(sample_volume_gallons)
    print(converted_liters)
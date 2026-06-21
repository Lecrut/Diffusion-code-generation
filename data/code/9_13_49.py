class VolumeConverter:
    LITERS_PER_GALLON = 3.78541

    def __init__(self, gallons):
        if gallons < 0:
            raise ValueError("Gallons cannot be negative")
        self.gallons = gallons

    def convert_to_liters(self):
        return self.gallons * VolumeConverter.LITERS_PER_GALLON

if __name__ == '__main__':
    sample_gallons1 = 3.0
    converter1 = VolumeConverter(sample_gallons1)
    print(converter1.convert_to_liters())

    sample_gallons2 = 8.5
    converter2 = VolumeConverter(sample_gallons2)
    print(converter2.convert_to_liters())
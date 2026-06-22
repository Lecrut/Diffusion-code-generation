class VolumeConverter:
    LITERS_PER_GALLON = 3.78541

    @staticmethod
    def _validate_gallons(gallons):
        if not isinstance(gallons, (int, float)):
            raise TypeError("Gallons must be a number")
        if gallons < 0:
            raise ValueError("Gallons cannot be negative")

    @classmethod
    def gallons_to_liters(cls, gallons):
        cls._validate_gallons(gallons)
        return gallons * cls.LITERS_PER_GALLON

if __name__ == '__main__':
    sample_gallons = 8.0
    converter = VolumeConverter()
    converted_liters = converter.gallons_to_liters(sample_gallons)
    print(converted_liters)
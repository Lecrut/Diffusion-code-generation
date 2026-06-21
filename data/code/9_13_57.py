class VolumeConverter:
    LITERS_PER_GALLON = 3.78541

    @staticmethod
    def validate_input(gallons):
        if not isinstance(gallons, (int, float)):
            raise TypeError("Input must be a number")
        if gallons < 0:
            raise ValueError("Gallons cannot be negative")

    @classmethod
    def convert_gallons_to_liters(cls, gallons):
        cls.validate_input(gallons)
        return gallons * cls.LITERS_PER_GALLON

if __name__ == '__main__':
    sample_volume_gallons = 15.0
    converter = VolumeConverter()
    try:
        converted_liters = converter.convert_gallons_to_liters(sample_volume_gallons)
        print(converted_liters)
    except Exception as e:
        print(e)
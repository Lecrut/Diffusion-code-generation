class VolumeUnitConverter:
    @staticmethod
    def _validate_volume_input(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be a number")
        if value < 0:
            raise ValueError("Volume cannot be negative")
        return float(value)

    @staticmethod
    def liters_to_milliliters(liters):
        validated_liters = VolumeUnitConverter._validate_volume_input(liters)
        return validated_liters * 1000.0

if __name__ == '__main__':
    converter = VolumeUnitConverter()
    sample_value_1 = 1.5
    result_1 = converter.liters_to_milliliters(sample_value_1)
    print(result_1)
    sample_value_2 = 0.25
    result_2 = converter.liters_to_milliliters(sample_value_2)
    print(result_2)
    sample_value_3 = 100
    result_3 = converter.liters_to_milliliters(sample_value_3)
    print(result_3)
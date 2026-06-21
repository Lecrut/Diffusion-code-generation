class VolumeConverter:
    CONVERSION_FACTOR = 0.0610237440947

    @staticmethod
    def cubic_centimeters_to_cubic_inches(cubic_centimeters):
        return cubic_centimeters * VolumeConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    sample_values = [50, 200, 800]
    converter = VolumeConverter()
    for value in sample_values:
        result = converter.cubic_centimeters_to_cubic_inches(value)
        print(f'{value} cubic centimeters is {result:.6f} cubic inches')
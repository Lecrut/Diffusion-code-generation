class NauticalMilesConverter:
    CONVERSION_FACTOR = 1.852

    @staticmethod
    def convert(nautical_miles):
        if not isinstance(nautical_miles, (int, float)):
            raise ValueError("Input must be an integer or floating-point number")
        return round(nautical_miles * NauticalMilesConverter.CONVERSION_FACTOR, 2)

if __name__ == '__main__':
    converter = NauticalMilesConverter()
    print(converter.convert(10))
    print(converter.convert(5.5))
    print(converter.convert(3.75))
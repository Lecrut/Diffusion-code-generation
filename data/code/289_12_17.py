class DistanceConverter:

    def inches_to_centimeters(self, inches):
        return round(inches * 2.54, 1)
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.inches_to_centimeters(1))
    print(converter.inches_to_centimeters(5))
    print(converter.inches_to_centimeters(10.5))
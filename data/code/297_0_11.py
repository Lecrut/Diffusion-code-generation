class LengthConverter:
    M_TO_KM = 1 / 1000

    @staticmethod
    def convert_meters_to_kilometers(meters):
        return meters * LengthConverter.M_TO_KM
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert_meters_to_kilometers(1500))
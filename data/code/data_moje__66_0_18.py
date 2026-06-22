class DistanceConverter:
    METERS_PER_KILOMETER = 1000

    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers * DistanceConverter.METERS_PER_KILOMETER

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.kilometers_to_meters(10.5))
class DistanceConverter:
    KILOMETERS_TO_MILES_FACTOR = 5

    def convert(self, kilometers):
        return kilometers * self.KILOMETERS_TO_MILES_FACTOR

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10))
    print(converter.convert(100))
    print(converter.convert(0))
    print(converter.convert(1))
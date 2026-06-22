class DistanceConverter:

    def convert(self, yards):
        return yards * 0.0009144
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1))
    print(converter.convert(5))
    print(converter.convert(10))
    print(converter.convert(100))
    print(converter.convert(1000))
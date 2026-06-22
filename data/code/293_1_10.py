class DistanceConverter:

    def convert_to_miles(self, kilometers):
        return kilometers * 0.621371

    def convert_to_kilometers(self, miles):
        return miles / 0.621371
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert_to_miles(10))
    print(converter.convert_to_kilometers(5))
class LengthConverter:

    def meters_to_kilometers(self, value):
        return value / 1000
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.meters_to_kilometers(500))
    print(converter.meters_to_kilometers(1000))
    print(converter.meters_to_kilometers(2500))
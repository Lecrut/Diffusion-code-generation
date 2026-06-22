class DistanceConverter:

    def miles_to_kilometers(self, miles):
        return miles * 1.60934
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_kilometers(5))
    print(converter.miles_to_kilometers(10))
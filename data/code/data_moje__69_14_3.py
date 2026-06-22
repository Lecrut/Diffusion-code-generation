class DistanceConverter:
    @staticmethod
    def miles_to_feet(miles):
        return miles * 5280

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.miles_to_feet(1)
    print(result)
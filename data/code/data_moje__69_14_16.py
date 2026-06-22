class DistanceConverter:
    @staticmethod
    def miles_to_feet(miles):
        return miles * 5280

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_miles = 10
    result_feet = converter.miles_to_feet(sample_miles)
    print(result_feet)
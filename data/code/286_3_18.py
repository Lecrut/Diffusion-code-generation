class DistanceConverter:
    MILE_TO_KM = 1.60934

    @staticmethod
    def convert_miles_to_km(miles):
        if not isinstance(miles, (int, float)):
            raise ValueError("Invalid input type. Expected int or float.")
        return miles * DistanceConverter.MILE_TO_KM

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert_miles_to_km(10))
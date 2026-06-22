class DistanceConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        if miles < 0:
            raise ValueError("Input cannot be negative")
        return miles * 5280

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.miles_to_feet(2)
    print(result)
    print(DistanceConverter.miles_to_feet(1.5))
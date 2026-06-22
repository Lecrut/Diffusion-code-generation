class DistanceConverter:
    @staticmethod
    def miles_to_feet(miles):
        if miles < 0:
            raise ValueError("Miles cannot be negative")
        feet = miles * 5280
        return feet

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.miles_to_feet(1)
    print(result)
    result2 = DistanceConverter.miles_to_feet(2)
    print(result2)
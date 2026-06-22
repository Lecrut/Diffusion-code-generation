class UnitConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type")
        if miles < 0:
            raise ValueError("Input cannot be negative")
        return miles * 5280

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.miles_to_feet(5)
    print(result)
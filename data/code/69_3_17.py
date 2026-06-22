class Converter:
    @staticmethod
    def convert_miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float).")
        if miles < 0:
            raise ValueError("Input cannot be negative.")
        return miles * 5280

if __name__ == '__main__':
    sample_miles = 3.5
    result = Converter.convert_miles_to_feet(sample_miles)
    print(result)
class MileConverter:
    @staticmethod
    def to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float).")
        if miles < 0:
            raise ValueError("Miles cannot be negative.")
        return miles * 5280

if __name__ == '__main__':
    converter = MileConverter()
    sample_miles = 12.5
    feet_result = converter.to_feet(sample_miles)
    print(feet_result)
    try:
        invalid_result = converter.to_feet("5")
    except TypeError as e:
        print(e)
    try:
        negative_result = converter.to_feet(-5)
    except ValueError as e:
        print(e)
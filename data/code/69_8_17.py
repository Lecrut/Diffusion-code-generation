class UnitConverter:
    def __init__(self):
        self.miles_to_feet_factor = 5280

    def convert_miles_to_feet(self, miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * self.miles_to_feet_factor

if __name__ == '__main__':
    converter = UnitConverter()
    sample_miles = 5
    result_feet = converter.convert_miles_to_feet(sample_miles)
    print(result_feet)
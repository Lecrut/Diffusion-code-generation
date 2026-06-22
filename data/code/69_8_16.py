class UnitConverter:
    def __init__(self):
        self.miles_to_feet_factor = 5280

    def convert_miles_to_feet(self, miles):
        return miles * self.miles_to_feet_factor

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert_miles_to_feet(2)
    print(result)
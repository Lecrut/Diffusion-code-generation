class UnitConverter:
    def convert_miles_to_feet(self, miles):
        return miles * 5280

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert_miles_to_feet(1)
    print(result)
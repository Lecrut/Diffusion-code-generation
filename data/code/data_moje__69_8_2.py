class UnitConverter:
    def miles_to_feet(self, miles):
        return miles * 5280

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.miles_to_feet(2)
    print(result)
class MileToFootConverter:
    def __init__(self):
        self.conversion_factor = 5280

    def convert(self, miles):
        return miles * self.conversion_factor

if __name__ == '__main__':
    converter = MileToFootConverter()
    miles_value = 5
    feet_value = converter.convert(miles_value)
    print(feet_value)
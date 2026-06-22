class MilesToFeetConverter:
    def convert(self, miles):
        return miles * 5280

if __name__ == '__main__':
    converter = MilesToFeetConverter()
    miles_value = 10
    result = converter.convert(miles_value)
    print(result)
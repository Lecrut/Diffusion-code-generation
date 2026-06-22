class MilesToFeetConverter:
    def convert(self, miles):
        return miles * 5280

if __name__ == '__main__':
    converter = MilesToFeetConverter()
    result = converter.convert(3.5)
    print(result)
    result_two = converter.convert(10)
    print(result_two)
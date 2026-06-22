class MileToFeetConverter:
    def convert(self, miles):
        return miles * 5280

if __name__ == '__main__':
    converter = MileToFeetConverter()
    sample_miles = 3
    result = converter.convert(sample_miles)
    print(result)
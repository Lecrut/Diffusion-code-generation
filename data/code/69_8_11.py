class MileToFeetConverter:
    def convert(self, miles):
        return miles * 5280

if __name__ == '__main__':
    converter = MileToFeetConverter()
    result = converter.convert(5)
    print(result)
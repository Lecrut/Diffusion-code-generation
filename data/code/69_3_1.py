class MileToFootConverter:
    @staticmethod
    def convert(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type")
        if isinstance(miles, bool):
            raise TypeError("Input must be a numeric type")
        return miles * 5280

if __name__ == '__main__':
    converter = MileToFootConverter()
    result1 = converter.convert(1)
    print(result1)
    result2 = converter.convert(2.5)
    print(result2)
    try:
        converter.convert("invalid")
    except TypeError as e:
        print(e)
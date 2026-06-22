class MileToFootConverter:
    @staticmethod
    def convert(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float)")
        if isinstance(miles, bool):
            raise TypeError("Input must be a numeric type (int or float), not bool")
        return miles * 5280

if __name__ == '__main__':
    converter = MileToFootConverter()
    print(converter.convert(1))
    print(converter.convert(2.5))
    print(converter.convert(0))
    print(converter.convert(-1))
    try:
        converter.convert("5")
    except TypeError as e:
        print(str(e))
    try:
        converter.convert(True)
    except TypeError as e:
        print(str(e))
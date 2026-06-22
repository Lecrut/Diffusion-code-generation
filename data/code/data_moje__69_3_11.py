class Converter:
    @staticmethod
    def mile_to_foot(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        if isinstance(miles, bool):
            raise TypeError("Input must be a number")
        return miles * 5280

if __name__ == '__main__':
    result = Converter.mile_to_foot(2)
    print(result)
    result2 = Converter.mile_to_foot(1.5)
    print(result2)
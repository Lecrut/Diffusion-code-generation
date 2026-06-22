class UnitConverter:
    @staticmethod
    def mile_to_foot(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float)")
        if miles < 0:
            raise ValueError("Input cannot be negative")
        return miles * 5280

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.mile_to_foot(2)
    print(result)
    result_float = converter.mile_to_foot(1.5)
    print(result_float)
    try:
        converter.mile_to_foot("2")
    except TypeError as e:
        print(e)
    try:
        converter.mile_to_foot(-5)
    except ValueError as e:
        print(e)
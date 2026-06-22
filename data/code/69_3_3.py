class Converter:
    @staticmethod
    def mile_to_foot(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number.")
        if miles < 0:
            raise ValueError("Input must be non-negative.")
        return miles * 5280

if __name__ == '__main__':
    result = Converter.mile_to_foot(2)
    print(result)
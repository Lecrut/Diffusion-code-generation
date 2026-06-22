class Conversion:
    @staticmethod
    def mile_to_foot(distance):
        if not isinstance(distance, (int, float)):
            raise TypeError("Input must be a numeric type (int or float).")
        if distance < 0:
            raise ValueError("Input must be non-negative.")
        return distance * 5280

if __name__ == '__main__':
    result = Conversion.mile_to_foot(2.5)
    print(result)
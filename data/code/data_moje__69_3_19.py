class UnitConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        return miles * 5280

if __name__ == '__main__':
    result1 = UnitConverter.miles_to_feet(1)
    print(result1)
    result2 = UnitConverter.miles_to_feet(2.5)
    print(result2)
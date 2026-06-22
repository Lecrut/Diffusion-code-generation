class LengthConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        if miles < 0:
            raise ValueError("Input must be non-negative")
        return miles * 5280

if __name__ == '__main__':
    result = LengthConverter.miles_to_feet(2)
    print(result)
    result_negative = LengthConverter.miles_to_feet(-1)
    print(result_negative)
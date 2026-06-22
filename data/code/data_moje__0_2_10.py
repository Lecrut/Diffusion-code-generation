INCH_TO_CM_FACTOR = 2.54

class LengthConverter:
    @staticmethod
    def convert_inches_to_cm(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number")
        if value < 0:
            raise ValueError("Length cannot be negative")
        return value * INCH_TO_CM_FACTOR

if __name__ == '__main__':
    converter = LengthConverter()
    test_values = [5, 12.5, 0.1]
    for val in test_values:
        try:
            result = converter.convert_inches_to_cm(val)
            print(f"{val} inches is {result} cm")
        except ValueError as e:
            print(f"Error with {val}: {e}")
    
    try:
        converter.convert_inches_to_cm("invalid")
    except TypeError as e:
        print(f"Error with 'invalid': {e}")
    
    try:
        converter.convert_inches_to_cm(-5)
    except ValueError as e:
        print(f"Error with -5: {e}")
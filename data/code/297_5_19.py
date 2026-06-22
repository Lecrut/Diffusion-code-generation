def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError('Input must be a number')

def inches_to_centimeters(inches):
    validate_input(inches)
    return inches * 2.54
if __name__ == '__main__':
    print(inches_to_centimeters(1))
    print(inches_to_centimeters(0))
    print(inches_to_centimeters(10))
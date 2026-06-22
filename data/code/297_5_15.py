def validate_inch_value(inches):
    if not isinstance(inches, (int, float)) or inches < 0:
        raise ValueError("Inch value must be a non-negative number")

def inches_to_centimeters(inches):
    validate_inch_value(inches)
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = 5
    print(inches_to_centimeters(sample_inches))
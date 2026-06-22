INCHES_TO_CM = 2.54

def validate_inch_value(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Invalid inch value")

def inches_to_cm(inches):
    validate_inch_value(inches)
    return inches * INCHES_TO_CM

if __name__ == '__main__':
    sample_inches = 5
    print(f"{sample_inches} inches is {inches_to_cm(sample_inches)} cm")
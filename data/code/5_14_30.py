def compare_lengths(inches, centimeters):
    INCH_TO_CM = 2.54
    normalized_inch_length = inches * INCH_TO_CM
    if normalized_inch_length > centimeters:
        return 'Inches is longer.'
    elif normalized_inch_length < centimeters:
        return 'Centimeters is longer.'
    else:
        return 'Both are equal.'
if __name__ == '__main__':
    inches_value = 10
    centimeters_value = 25
    result = compare_lengths(inches_value, centimeters_value)
    print(result)
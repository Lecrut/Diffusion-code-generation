def compare_lengths(inches, centimeters):
    INCH_TO_CM = 2.54
    normalized_inch_length = inches * INCH_TO_CM
    if normalized_inch_length > centimeters:
        return 'Inches is greater than Centimeters'
    elif normalized_inch_length < centimeters:
        return 'Centimeters is greater than Inches'
    else:
        return 'Both are equal'
if __name__ == '__main__':
    inches = 10
    centimeters = 25
    result = compare_lengths(inches, centimeters)
    print(result)
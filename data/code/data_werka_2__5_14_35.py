def compare_lengths(inches, centimeters):
    INCH_TO_CM = 2.54
    normalized_inches = inches * INCH_TO_CM
    if normalized_inches > centimeters:
        return 'Inches is greater than Centimeters'
    elif normalized_inches < centimeters:
        return 'Centimeters is greater than Inches'
    else:
        return 'Both are equal'
if __name__ == '__main__':
    inches = 10
    centimeters = 25.4
    result = compare_lengths(inches, centimeters)
    print(result)
def compare_lengths(inches, centimeters):
    inches_to_cm = 2.54
    normalized_inch_length = inches * inches_to_cm
    if normalized_inch_length > centimeters:
        return "Inches is longer"
    elif normalized_inch_length < centimeters:
        return "Centimeters is longer"
    else:
        return "Both are equal"

if __name__ == '__main__':
    inches_value = 10
    cm_value = 25.4
    result = compare_lengths(inches_value, cm_value)
    print(result)
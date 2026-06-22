def compare_lengths(inches, centimeters):
    inches_to_cm = 2.54
    normalized_inches = inches * inches_to_cm
    if normalized_inches > centimeters:
        return "Inches is longer"
    elif normalized_inches < centimeters:
        return "Centimeters is longer"
    else:
        return "Both are equal"

if __name__ == '__main__':
    inches_value = 10
    centimeters_value = 25.4
    result = compare_lengths(inches_value, centimeters_value)
    print(result)
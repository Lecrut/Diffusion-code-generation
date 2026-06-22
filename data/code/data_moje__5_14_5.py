def normalize_inches_to_cm(value_in_inches):
    return value_in_inches * 2.54

def compare_lengths(inches_value, cm_value):
    normalized_inches_to_cm = normalize_inches_to_cm(inches_value)
    if normalized_inches_to_cm > cm_value:
        return f"{inches_value} inches ({normalized_inches_to_cm:.2f} cm) is greater than {cm_value} cm"
    elif normalized_inches_to_cm < cm_value:
        return f"{inches_value} inches ({normalized_inches_to_cm:.2f} cm) is less than {cm_value} cm"
    else:
        return f"{inches_value} inches ({normalized_inches_to_cm:.2f} cm) is equal to {cm_value} cm"

if __name__ == '__main__':
    inches_val = 10
    cm_val = 25
    result = compare_lengths(inches_val, cm_val)
    print(result)
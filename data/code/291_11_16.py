def validate_input(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Input must be a numeric value")

def compare_lengths(length1, length2):
    length1 = validate_input(length1)
    length2 = validate_input(length2)
    
    if length1 > length2:
        return round(length1, 2), "longer"
    elif length2 > length1:
        return round(length2, 2), "longer"
    else:
        return round(length1, 2), "equal"

if __name__ == '__main__':
    print(compare_lengths(10.5, 20.3))
    print(compare_lengths(30, 15))
    print(compare_lengths(5.75, 5.75))
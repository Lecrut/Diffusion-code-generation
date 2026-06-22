def validate_positive(value):
    if value <= 0:
        raise ValueError("Both lengths must be positive")

def calculate_ratio(length1, length2):
    validate_positive(length1)
    validate_positive(length2)
    return length1 / length2

if __name__ == '__main__':
    try:
        ratio = calculate_ratio(15, 3)
        print(ratio)
    except ValueError as e:
        print(e)
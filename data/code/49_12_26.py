def validate_lengths(length1, length2):
    if not isinstance(length1, (int, float)):
        raise ValueError("Length1 must be an integer or float.")
    if not isinstance(length2, (int, float)):
        raise ValueError("Length2 must be an integer or float.")
    if length2 == 0:
        raise ValueError("Length2 cannot be zero.")

def calculate_ratio(length1, length2):
    validate_lengths(length1, length2)
    return length1 / length2

if __name__ == '__main__':
    length1 = 20.75
    length2 = 4.25
    try:
        ratio = calculate_ratio(length1, length2)
        print(f"The ratio of {length1} to {length2} is: {ratio:.10f}")
    except ValueError as e:
        print(e)
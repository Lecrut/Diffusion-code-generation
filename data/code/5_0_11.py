def calculate_length_difference(length1, length2):
    try:
        val1 = float(length1)
    except (TypeError, ValueError):
        raise ValueError("First length must be numeric")
    try:
        val2 = float(length2)
    except (TypeError, ValueError):
        raise ValueError("Second length must be numeric")
    return abs(val1 - val2)

if __name__ == '__main__':
    result = calculate_length_difference(10.5, 5.2)
    print(result)
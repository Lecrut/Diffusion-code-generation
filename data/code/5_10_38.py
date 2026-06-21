def calculate_length_difference(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return abs(a - b)

if __name__ == '__main__':
    try:
        length1 = 20
        length2 = 7
        result = calculate_length_difference(length1, length2)
        print(result)
    except ValueError as e:
        print(e)
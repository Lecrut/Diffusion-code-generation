def validate_input(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be integers or floats")

def compare_values(a, b):
    validate_input(a, b)
    difference = a - b
    return 1 if difference > 0 else (-1 if difference < 0 else 0)

if __name__ == '__main__':
    result1 = compare_values(7, 3)
    print(result1)
    result2 = compare_values(4, 4)
    print(result2)
    result3 = compare_values(9, 15)
    print(result3)
def validate_input(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be integers or floats")

def compare_values(a, b):
    validate_input(a, b)
    return (a > b) - (a < b)

if __name__ == '__main__':
    result1 = compare_values(10, 5)
    print(result1)
    result2 = compare_values(7, 7)
    print(result2)
    result3 = compare_values(3, 9)
    print(result3)
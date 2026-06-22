def validate_sides(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("All sides must be positive numbers.")

def calculate_perimeter(a, b, c):
    validate_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    try:
        result = calculate_perimeter(3.0, 4.0, 5.0)
        print(result)
    except ValueError as e:
        print(e)
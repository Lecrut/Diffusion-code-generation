SIDE_LENGTH_THRESHOLD = 0

def calculate_triangle_perimeter(a, b, c):
    if not all(side > SIDE_LENGTH_THRESHOLD for side in (a, b, c)):
        raise ValueError("All side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(6, 8, 10)
        print(perimeter)
    except ValueError as e:
        print(e)
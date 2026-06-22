def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle side lengths.")
    return a + b + c

if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(3, 4, 5)
        print(f"Perimeter for sides 3, 4, 5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result2 = calculate_perimeter(10, -2, 5)
        print(f"Perimeter for sides 10, -2, 5: {result2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result3 = calculate_perimeter(0, 4, 6)
        print(f"Perimeter for sides 0, 4, 6: {result3}")
    except ValueError as e:
        print(f"Error: {e}")
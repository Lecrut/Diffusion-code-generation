def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def calculate_triangle_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid side lengths. Cannot form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(6, 8, 10)
        print(perimeter)
    except ValueError as e:
        print(e)
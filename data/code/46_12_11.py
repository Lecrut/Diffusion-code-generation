MAX_ALLOWED_ERROR = 1e-9

def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def calculate_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError("The given sides do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    side_a = 3.0
    side_b = 4.0
    side_c = 5.0
    perimeter = calculate_perimeter(side_a, side_b, side_c)
    print(perimeter)
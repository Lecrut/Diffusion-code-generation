def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and (b + c > a)

def are_positive_numbers(a, b, c):
    return all((x > 0 for x in [a, b, c]))

def calculate_triangle_perimeter(a, b, c):
    if not are_positive_numbers(a, b, c):
        raise ValueError('Side lengths must be positive numbers.')
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7, 8, 9))
        print(calculate_triangle_perimeter(10, 6, 8))
        print(calculate_triangle_perimeter(1, 2, 3))
    except ValueError as e:
        print(e)
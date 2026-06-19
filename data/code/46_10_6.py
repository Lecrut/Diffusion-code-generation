def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in (a, b, c)):
        return None
    return a + b + c

if __name__ == '__main__':
    side_a = 7.5
    side_b = 9.2
    side_c = 4.8
    perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
    if perimeter is not None:
        print(perimeter)
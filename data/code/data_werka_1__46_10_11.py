def calculate_triangle_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    side_a = 7.0
    side_b = 8.0
    side_c = 9.0
    perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
    print(perimeter)
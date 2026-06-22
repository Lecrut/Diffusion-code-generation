def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    sides_1 = (3, 4, 5)
    sides_2 = (1, 2, 4)
    result_1 = is_valid_triangle(sides_1)
    result_2 = is_valid_triangle(sides_2)
    print(result_1)
    print(result_2)
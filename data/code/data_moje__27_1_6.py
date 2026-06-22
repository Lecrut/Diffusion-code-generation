def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    side_a = 3
    side_b = 4
    side_c = 5
    result = is_valid_triangle(side_a, side_b, side_c)
    print(result)
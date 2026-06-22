def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    result1 = is_valid_triangle(3, 4, 5)
    result2 = is_valid_triangle(1, 2, 3)
    result3 = is_valid_triangle(0, 1, 2)
    print(result1)
    print(result2)
    print(result3)
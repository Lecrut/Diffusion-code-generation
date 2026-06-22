def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    result1 = is_valid_triangle(3, 4, 5)
    print(result1)
    result2 = is_valid_triangle(1, 2, 3)
    print(result2)
    result3 = is_valid_triangle(5, 1, 1)
    print(result3)
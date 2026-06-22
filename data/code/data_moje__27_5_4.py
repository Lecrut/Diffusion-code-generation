def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    print(is_triangle(3, 4, 5))
    print(is_triangle(1, 2, 3))
    print(is_triangle(10, 11, 21))
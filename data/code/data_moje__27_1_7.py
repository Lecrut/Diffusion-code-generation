def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    sides1 = (3, 4, 5)
    sides2 = (1, 2, 3)
    sides3 = (10, 2, 1)
    print(is_valid_triangle(*sides1))
    print(is_valid_triangle(*sides2))
    print(is_valid_triangle(*sides3))
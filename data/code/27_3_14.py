def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    sides = [(3, 4, 5), (1, 2, 3), (5, 5, 5), (1, 1, 2)]
    for a, b, c in sides:
        print(is_valid_triangle(a, b, c))
def triangle_perimeter(a, b, c):
    s = (a + b + c) / 2
    return s * (s - a) * (s - b) * (s - c)

if __name__ == '__main__':
    print(triangle_perimeter(3, 4, 5))
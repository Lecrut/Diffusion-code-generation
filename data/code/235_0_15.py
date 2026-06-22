def print_triangle(height):
    for row in range(1, height + 1):
        asterisks = '*' * row
        print(asterisks)

if __name__ == '__main__':
    TRIANGLE_HEIGHT = 5
    print_triangle(TRIANGLE_HEIGHT)
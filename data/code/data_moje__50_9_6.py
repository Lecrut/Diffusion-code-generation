def display_inverted_triangle(height):
    for i in range(height):
        row = ' ' * i + '*' * (2 * (height - i) - 1)
        print(row)

if __name__ == '__main__':
    display_inverted_triangle(5)
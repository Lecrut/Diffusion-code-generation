def display_inverted_triangle(height):
    for row in range(height, 0, -1):
        print('* ' * row)

if __name__ == '__main__':
    display_inverted_triangle(5)
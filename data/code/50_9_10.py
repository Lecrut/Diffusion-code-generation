def display_inverted_triangle(height):
    rows = []
    for i in range(height, 0, -1):
        rows.append('* ' * i)
    return '\n'.join(rows)

if __name__ == '__main__':
    height = 5
    print(display_inverted_triangle(height))
def print_centered_triangle(levels):
    return [
        ' '.join(
            [' ' if i < levels - 1 - j else '*' for i in range(2 * levels - 1)]
        )
        for j in range(levels)
    ]

if __name__ == '__main__':
    levels = 12
    rows = print_centered_triangle(levels)
    for row in rows:
        print(row)
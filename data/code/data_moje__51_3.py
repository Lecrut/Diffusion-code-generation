def generate_pyramid(rows):
    max_width = len(str(2 * rows - 1))
    return '\n'.join(
        ''.join(
            str(i) if j == 0 or (i == j) or (i == rows - 1) or (j == rows - 1)
            else ' '
            for j in range(rows - i)
        ).center(max_width)
        for i in range(1, rows + 1)
    )

if __name__ == '__main__':
    print(generate_pyramid(7))
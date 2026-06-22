def print_downward_triangle(rows: int) -> None:
    for i in range(rows):
        spaces = ' ' * i
        stars = '*' * (2 * (rows - i) - 1)
        print(spaces + stars)

if __name__ == '__main__':
    row_count = 9
    print_downward_triangle(row_count)
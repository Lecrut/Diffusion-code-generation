def print_downward_triangle(row_count: int) -> None:
    for current_row in range(row_count, 0, -1):
        stars = '*' * current_row
        print(stars)

if __name__ == '__main__':
    print_downward_triangle(9)
def print_downward_triangle(row_count: int) -> None:
    for i in range(row_count):
        print("* " * (row_count - i))

if __name__ == '__main__':
    print_downward_triangle(9)
def print_reverse_triangle(rows: int) -> None:
    for i in range(rows, 0, -1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(num) for num in range(i, 0, -1))
        print(spaces + numbers)

if __name__ == '__main__':
    print_reverse_triangle(4)
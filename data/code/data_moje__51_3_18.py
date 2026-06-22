def print_centered_number_pyramid(rows: int = 7) -> None:
    for i in range(1, rows + 1):
        numbers = [str(j) for j in range(1, i + 1)]
        line = ''.join(numbers)
        max_width = (rows * 2) - 1
        print(line.center(max_width))

if __name__ == '__main__':
    print_centered_number_pyramid(7)
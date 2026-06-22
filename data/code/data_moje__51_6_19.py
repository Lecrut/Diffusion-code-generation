def print_number_pyramid(levels: int) -> None:
    for row in range(1, levels + 1):
        spaces = ' ' * (levels - row)
        numbers = [str(num) for num in range(1, row + 1)]
        line = ' '.join(numbers)
        print(spaces + line)

if __name__ == '__main__':
    print_number_pyramid(4)
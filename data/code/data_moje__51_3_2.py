def print_number_pyramid(rows=7):
    return '\n'.join(
        ' '.join([str(i)] * (2 * i - 1)).center(rows * 2 - 1)
        for i in range(1, rows + 1)
    )

if __name__ == '__main__':
    print(print_number_pyramid(7))
def print_number_pyramid(rows: int) -> str:
    lines = [
        ' '.join(str(j) for j in range(1, i + 1)).center(rows * 2 - 1)
        for i in range(1, rows + 1)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_number_pyramid(7)
    print(result)
def print_triangle(size: int) -> None:
    for i in range(1, size + 1):
        row = ''
        for j in range(i):
            char = chr(ord('A') + j % 26)
            row += char + ' '
        print(row.strip())
if __name__ == '__main__':
    print_triangle(5)
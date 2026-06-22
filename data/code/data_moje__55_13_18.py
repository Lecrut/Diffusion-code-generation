def print_triangle(n: int) -> None:
    current = 0
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(chr(ord('A') + current % 26))
            current += 1
        print(' '.join(row))
if __name__ == '__main__':
    print_triangle(5)
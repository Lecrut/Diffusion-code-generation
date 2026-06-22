def print_triangle(n):
    start = ord('A')
    current = start
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(chr(current))
            current += 1
            if current > ord('Z'):
                current = start
        print(' '.join(row))

if __name__ == '__main__':
    print_triangle(5)
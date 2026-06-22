def print_pyramid(n):
    lines = [
        ''.join([
            chr(65 + abs(i - (n - 1))) if abs(i - (n - 1)) < j else ' '
            for i in range(n)
        ])
        for j, n_val in enumerate(range(n))
    ]
    for line in lines:
        print(line)

if __name__ == '__main__':
    print_pyramid(5)
def number_pyramid(n):
    return '\n'.join(
        ''.join(str((i + 1) if j == 0 else i + 1) for j in range(1, 2 * (i + 1))) for i in range(n)
    )

if __name__ == '__main__':
    n = 7
    lines = number_pyramid(n).split('\n')
    max_width = len(lines[-1])
    for line in lines:
        print(line.center(max_width))
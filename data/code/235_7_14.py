def generate_checkerboard(size):
    pattern = []
    for i in range(size):
        row = ['X' if (i + j) % 2 == 0 else '.' for j in range(size)]
        pattern.append(''.join(row))
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_checkerboard(4))
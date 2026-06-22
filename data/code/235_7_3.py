def checkerboard(size):
    pattern = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append('X')
            else:
                row.append('.')
        pattern.append(''.join(row))
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(checkerboard(4))
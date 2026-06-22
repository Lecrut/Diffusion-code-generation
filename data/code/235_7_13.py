def generate_checkerboard(size):
    pattern = []
    for i in range(size):
        row = ''
        for j in range(size):
            if (i + j) % 2 == 0:
                row += 'X'
            else:
                row += '.'
        pattern.append(row)
    return '\n'.join(pattern)

if __name__ == '__main__':
    sample_size = 4
    checkerboard_pattern = generate_checkerboard(sample_size)
    print(checkerboard_pattern)
def generate_pattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                print('*', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    sample_rows = 10
    sample_cols = 10
    generate_pattern(sample_rows, sample_cols)
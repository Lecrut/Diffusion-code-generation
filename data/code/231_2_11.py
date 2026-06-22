def generate_pattern(rows=10, cols=10):
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                print('*', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    generate_pattern()
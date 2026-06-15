def generate_pattern(rows, cols, char='*'):
    for i in range(rows):
        for j in range(cols):
            print(char, end='')
        print()
if __name__ == '__main__':
    generate_pattern(3, 4)
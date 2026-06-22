def zigzag_line(width):
    for i in range(width):
        if i % 2 == 0:
            print('*' * (i + 1))
        else:
            print(' ' * (width - i - 1) + '*' * (i + 1))

if __name__ == '__main__':
    zigzag_line(5)
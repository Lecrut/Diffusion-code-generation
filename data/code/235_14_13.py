def zigzag_line(width):
    for i in range(width):
        if i % 2 == 0:
            print('*' * (width - i) + ' ' * (i * 2))
        else:
            print(' ' * (i * 2) + '*' * (width - i))

if __name__ == '__main__':
    zigzag_line(10)
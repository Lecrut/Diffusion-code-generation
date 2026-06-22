def print_square(size):
    if size <= 0:
        return
    for _ in range(size):
        print('*' * size)

if __name__ == '__main__':
    print_square(5)
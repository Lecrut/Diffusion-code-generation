def print_square(n):
    return (('*' * n + '\n') * n).rstrip()

if __name__ == '__main__':
    print(print_square(7))
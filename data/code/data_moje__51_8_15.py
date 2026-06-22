def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        print(' '.join(str(i) for _ in range(i)))

if __name__ == '__main__':
    print_number_pyramid(5)
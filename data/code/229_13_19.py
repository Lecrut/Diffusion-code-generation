def print_grid(size):
    if size <= 0:
        raise ValueError("Grid size must be greater than zero.")
    
    for i in range(size):
        for j in range(size):
            print('*', end='')
            if j < size - 1:
                print(' | ', end='')
        print()
        if i < size - 1:
            print('-' * (4 * size + 3))

if __name__ == '__main__':
    try:
        print_grid(15)
    except ValueError as e:
        print(e)
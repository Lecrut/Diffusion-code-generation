def hollow_square_generator(size: int):
    if size <= 0:
        return
    for row_index in range(size):
        if row_index == 0 or row_index == size - 1:
            yield '*' * size
        else:
            yield '*' + ' ' * (size - 2) + '*'

if __name__ == '__main__':
    sample_size = 7
    for row in hollow_square_generator(sample_size):
        print(row)
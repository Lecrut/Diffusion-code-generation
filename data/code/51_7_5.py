def right_aligned_pyramid_generator(rows=8):
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + str(i) * i
        yield line

if __name__ == '__main__':
    for chunk in right_aligned_pyramid_generator(8):
        print(chunk)
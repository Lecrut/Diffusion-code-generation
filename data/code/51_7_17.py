def number_pyramid_generator(rows):
    for i in range(1, rows + 1):
        line = " " * (rows - i) + str(i) * i
        yield line

if __name__ == '__main__':
    target_rows = 8
    for chunk in number_pyramid_generator(target_rows):
        print(chunk)
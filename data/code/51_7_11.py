def number_pyramid_chunks(rows=8):
    max_width = rows * 2 - 1
    for i in range(1, rows + 1):
        line = str(i) * (2 * i - 1)
        padded = line.rjust(max_width)
        yield padded + '\n'

if __name__ == '__main__':
    result = list(number_pyramid_chunks(8))
    for chunk in result:
        print(chunk, end='')
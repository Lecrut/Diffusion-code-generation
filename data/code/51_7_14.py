def pyramid_chunk_generator(rows=8):
    max_width = 2 * rows - 1
    for i in range(1, rows + 1):
        line = str(i) * (2 * i - 1)
        padded_line = line.rjust(max_width)
        yield padded_line + '\n'

if __name__ == '__main__':
    chunks = list(pyramid_chunk_generator())
    print(''.join(chunks), end='')
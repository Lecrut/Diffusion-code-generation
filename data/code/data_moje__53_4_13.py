import itertools

def generate_reverse_triangle(height):
    for i in range(height, 0, -1):
        row_chars = itertools.chain.from_iterable(itertools.repeat(str(j), j) for j in range(1, i + 1))
        yield "".join(row_chars)

if __name__ == '__main__':
    sample_height = 3
    for line in generate_reverse_triangle(sample_height):
        print(line)
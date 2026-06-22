import itertools

def generate_reverse_triangle(height):
    for i in range(height, 0, -1):
        row_numbers = itertools.chain.from_iterable(itertools.repeat(str(j), j) for j in range(1, i + 1))
        yield "".join(row_numbers)

if __name__ == '__main__':
    for row_string in generate_reverse_triangle(3):
        print(row_string)
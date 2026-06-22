import itertools

def generate_reverse_number_triangle(height):
    for i in range(height, 0, -1):
        numbers = itertools.chain(range(i), itertools.repeat('', 0))
        row_str = " ".join(str(n) for n in range(1, i + 1))
        yield row_str

if __name__ == '__main__':
    for row in generate_reverse_number_triangle(3):
        print(row)
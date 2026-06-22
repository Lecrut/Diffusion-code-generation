import itertools

def generate_reverse_number_triangle(height):
    for row_index in range(height, 0, -1):
        numbers = itertools.chain(range(row_index, 0, -1))
        row_string = " ".join(str(n) for n in numbers)
        yield row_string

if __name__ == '__main__':
    height = 3
    for row in generate_reverse_number_triangle(height):
        print(row)
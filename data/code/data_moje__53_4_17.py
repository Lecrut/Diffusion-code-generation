import itertools

def generate_reverse_number_triangle(height):
    for i in range(height, 0, -1):
        row_numbers = itertools.chain.from_iterable([range(i, 0, -1) for _ in range(i)])
        row_string = "".join(str(num) for num in range(i, 0, -1))
        yield row_string

if __name__ == '__main__':
    triangle_height = 3
    for row in generate_reverse_number_triangle(triangle_height):
        print(row)
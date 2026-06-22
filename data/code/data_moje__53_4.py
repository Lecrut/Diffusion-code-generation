import itertools

def reverse_number_triangle(height):
    for row_index in range(height, 0, -1):
        chars = itertools.chain.from_iterable(reversed(range(1, row_index + 1)))
        yield "".join(str(num) for num in chars)

if __name__ == '__main__':
    height_value = 3
    for line in reverse_number_triangle(height_value):
        print(line)
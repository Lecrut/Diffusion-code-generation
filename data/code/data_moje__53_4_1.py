import itertools

def generate_reverse_triangle(height):
    for i in range(height, 0, -1):
        row_numbers = list(itertools.chain(range(i, 0, -1)))
        row_string = ' '.join(str(num) for num in row_numbers)
        yield row_string

if __name__ == '__main__':
    height = 3
    for row in generate_reverse_triangle(height):
        print(row)
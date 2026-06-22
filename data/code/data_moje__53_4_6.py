import itertools

def generate_reverse_triangle(height):
    for i in range(height, 0, -1):
        row_numbers = itertools.chain(range(i, 0, -1))
        yield " ".join(map(str, row_numbers))

if __name__ == "__main__":
    height_value = 3
    for row_string in generate_reverse_triangle(height_value):
        print(row_string)
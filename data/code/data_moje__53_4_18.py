import itertools

def generate_reverse_number_triangle(height):
    for row_num in range(height, 0, -1):
        numbers = itertools.count(1)
        row_list = [str(next(numbers)) for _ in range(row_num)]
        yield " ".join(row_list)

if __name__ == '__main__':
    for line in generate_reverse_number_triangle(3):
        print(line)
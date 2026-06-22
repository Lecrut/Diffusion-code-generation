import itertools

def generate_reverse_number_triangle(height):
    rows = []
    for row_num in range(height, 0, -1):
        numbers = list(itertools.chain.from_iterable(range(i) for i in range(1, row_num + 1)))
        number_str = " ".join(str(n) for n in numbers)
        rows.append(number_str)
    return rows

if __name__ == '__main__':
    sample_height = 3
    result = generate_reverse_number_triangle(sample_height)
    for line in result:
        print(line)
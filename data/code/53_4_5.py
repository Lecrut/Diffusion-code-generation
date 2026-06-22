import itertools

def generate_reverse_triangle(height):
    rows = []
    for i in range(height, 0, -1):
        row_numbers = itertools.chain.from_iterable([str(x) for x in range(1, i + 1)])
        rows.append("".join(row_numbers))
    return rows

if __name__ == '__main__':
    height = 3
    result = generate_reverse_triangle(height)
    for line in result:
        print(line)
import itertools

def generate_reverse_triangle(height):
    result = []
    for row_index in range(height, 0, -1):
        numbers = itertools.chain(range(1, row_index + 1))
        row_string = ' '.join(str(n) for n in numbers)
        result.append(row_string)
    return result

if __name__ == '__main__':
    triangle_lines = generate_reverse_triangle(3)
    for line in triangle_lines:
        print(line)
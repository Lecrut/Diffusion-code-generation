from itertools import chain, repeat

def generate_reverse_number_triangle(height=3):
    rows = []
    for i in range(height, 0, -1):
        row = ''.join(map(str, range(1, i + 1)))
        rows.append(row)
    return rows

if __name__ == '__main__':
    result = generate_reverse_number_triangle(3)
    for row in result:
        print(row)
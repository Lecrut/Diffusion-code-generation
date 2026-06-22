import itertools

def reverse_number_triangle(height=3):
    result = []
    numbers = list(range(1, height + 1))
    for i in range(height, 0, -1):
        row_numbers = numbers[:i]
        row_str = ' '.join(map(str, row_numbers))
        result.append(row_str)
    return result

if __name__ == '__main__':
    rows = reverse_number_triangle(3)
    for row in rows:
        print(row)
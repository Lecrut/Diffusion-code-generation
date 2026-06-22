import itertools

def reverse_number_triangle(height):
    rows = []
    for i in range(1, height + 1):
        nums = range(i, 0, -1)
        row_str = ' '.join(map(str, nums))
        rows.append(row_str)
    return rows
if __name__ == '__main__':
    height = 3
    result = reverse_number_triangle(height)
    print(result)
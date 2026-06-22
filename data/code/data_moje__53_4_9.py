import itertools

def reverse_number_triangle(height):
    rows = []
    current_number = height
    for i in range(height, 0, -1):
        row = [current_number] * i
        rows.append(' '.join(map(str, row)))
        current_number -= 1
    return rows

if __name__ == '__main__':
    result = reverse_number_triangle(3)
    for line in result:
        print(line)
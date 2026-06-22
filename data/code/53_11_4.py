def generate_reverse_triangle_pattern(height):
    result = []
    for i in range(height, 0, -1):
        row = list(range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    height = 5
    pattern = generate_reverse_triangle_pattern(height)
    for row in pattern:
        print(' '.join(map(str, row)))
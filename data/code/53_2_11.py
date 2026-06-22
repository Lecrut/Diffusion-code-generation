def create_reverse_number_triangle(height):
    result = []
    for i in range(height, 0, -1):
        row = ' ' * (height - i) + ' '.join(str(j) for j in range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_height = 6
    lines = create_reverse_number_triangle(sample_height)
    for line in lines:
        print(line)
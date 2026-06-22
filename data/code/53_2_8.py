def generate_reverse_number_triangle(height):
    result = []
    for row in range(height, 0, -1):
        line = " ".join(str(num) for num in range(1, row + 1))
        result.append(line)
    return result

if __name__ == '__main__':
    sample_height = 6
    triangle_lines = generate_reverse_number_triangle(sample_height)
    for line in triangle_lines:
        print(line)
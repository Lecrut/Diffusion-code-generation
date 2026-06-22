def create_reverse_number_triangle(height):
    result = []
    for i in range(height, 0, -1):
        line = ' '.join(str(num) for num in range(1, i + 1))
        result.append(line)
    return result

if __name__ == '__main__':
    triangle = create_reverse_number_triangle(6)
    for line in triangle:
        print(line)
def generate_reverse_number_triangle(height):
    result = []
    for i in range(height, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(j)
        result.append(" ".join(map(str, row)))
    return "\n".join(result)

if __name__ == '__main__':
    TRIANGLE_HEIGHT = 5
    print(generate_reverse_number_triangle(TRIANGLE_HEIGHT))
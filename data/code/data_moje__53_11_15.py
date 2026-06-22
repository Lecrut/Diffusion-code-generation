def generate_reverse_triangle(height):
    result = []
    for i in range(height, 0, -1):
        row = []
        for j in range(i):
            row.append(str(j + 1))
        result.append(" ".join(row))
    return "\n".join(result)

if __name__ == '__main__':
    HEIGHT = 5
    print(generate_reverse_triangle(HEIGHT))
def generate_reverse_number_triangle(height):
    result = []
    for i in range(height, 0, -1):
        row = " ".join(str(j) for j in range(1, i + 1))
        result.append(row)
    return "\n".join(result)

if __name__ == '__main__':
    height = 4
    print(generate_reverse_number_triangle(height))
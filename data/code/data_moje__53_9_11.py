def generate_reverse_number_triangle(height):
    result = []
    for i in range(1, height + 1):
        row = []
        for j in range(height, 0, -1):
            if j >= i:
                row.append(str(j))
            else:
                row.append(" ")
        result.append(" ".join(row).rstrip())
    return result

if __name__ == '__main__':
    height = 5
    triangle = generate_reverse_number_triangle(height)
    for line in triangle:
        print(line)
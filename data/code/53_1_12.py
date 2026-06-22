def generate_right_aligned_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        spaces = " " * (rows - i)
        result.append(spaces + line)
    return result

if __name__ == '__main__':
    rows = 4
    lines = generate_right_aligned_reverse_triangle(rows)
    for line in lines:
        print(line)
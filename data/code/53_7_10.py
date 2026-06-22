def generate_reverse_number_triangle(rows):
    lines = []
    for i in range(rows, 0, -1):
        row_nums = []
        for j in range(1, i + 1):
            row_nums.append(str(j))
        lines.append(" ".join(row_nums))
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle(6)
    print(result)
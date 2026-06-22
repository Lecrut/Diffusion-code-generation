def generate_reverse_triangle(rows):
    lines = []
    for i in range(1, rows + 1):
        numbers = [str(j) for j in range(1, i + 1)]
        row_str = " ".join(numbers)
        max_width = len(" ".join([str(k) for k in range(1, rows + 1)]))
        padded_row = row_str.rjust(max_width)
        lines.append(padded_row)
    return "\n".join(lines)

if __name__ == '__main__':
    rows = 4
    result = generate_reverse_triangle(rows)
    print(result)
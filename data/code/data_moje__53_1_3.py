def generate_right_aligned_reverse_triangle(rows: int) -> str:
    result_lines = []
    for i in range(rows, 0, -1):
        numbers = []
        for j in range(1, i + 1):
            numbers.append(str(j))
        line_content = " ".join(numbers)
        padding = " " * (rows - i)
        formatted_line = padding + line_content
        result_lines.append(formatted_line)
    return "\n".join(result_lines)

if __name__ == '__main__':
    rows = 4
    output = generate_right_aligned_reverse_triangle(rows)
    print(output)
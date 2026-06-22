def generate_right_aligned_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_values = [str(j) for j in range(1, i + 1)]
        row_text = " ".join(row_values)
        padding = (rows - i)
        formatted_line = " " * (padding * 2) + row_text
        result.append(formatted_line)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_right_aligned_reverse_triangle(4))
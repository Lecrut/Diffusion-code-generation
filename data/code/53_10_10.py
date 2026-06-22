def generate_reverse_number_triangle(rows: int) -> str:
    lines = []
    for i in range(rows, 0, -1):
        line_parts = []
        for j in range(i, 0, -1):
            line_parts.append(str(j))
        lines.append(" ".join(line_parts))
    return "\n".join(lines)

if __name__ == "__main__":
    sample_rows = 5
    result = generate_reverse_number_triangle(sample_rows)
    print(result)
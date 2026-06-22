def generate_right_aligned_triangle(max_rows):
    if max_rows <= 0:
        return ""
    lines = []
    for i in range(1, max_rows + 1):
        chars = [chr(ord('A') + j) for j in range(i)]
        line = "".join(chars)
        padding = " " * (max_rows - i)
        lines.append(padding + line)
    return "\n".join(lines)

if __name__ == '__main__':
    max_rows = 5
    result = generate_right_aligned_triangle(max_rows)
    print(result)
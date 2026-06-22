def generate_reverse_number_triangle(n):
    if n <= 0:
        return ""
    lines = []
    for i in range(n, 0, -1):
        line = " ".join(str(j) for j in range(i, 0, -1))
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    sample_value = 5
    result = generate_reverse_number_triangle(sample_value)
    print(result)
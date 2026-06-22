def generate_reverse_number_triangle(height: int) -> list[str]:
    lines = []
    for i in range(height, 0, -1):
        row = " ".join(str(j) for j in range(1, i + 1))
        lines.append(row)
    return lines

if __name__ == "__main__":
    result = generate_reverse_number_triangle(6)
    for line in result:
        print(line)
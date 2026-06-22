def generate_reverse_number_triangle(height: int) -> str:
    lines = []
    for i in range(height, 0, -1):
        row = " ".join(str(num) for num in range(i, 0, -1))
        lines.append(row)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle(4)
    print(result)
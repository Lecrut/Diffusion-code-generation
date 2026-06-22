def generate_reverse_triangle(height: int = 4) -> str:
    lines = []
    for i in range(height, 0, -1):
        line = " ".join(str(i) for _ in range(i))
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_reverse_triangle(4)
    print(result)
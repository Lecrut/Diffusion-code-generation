def generate_reverse_triangle(height: int) -> str:
    lines = []
    for i in range(height, 0, -1):
        lines.append("* " * i)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_reverse_triangle(4)
    print(result)
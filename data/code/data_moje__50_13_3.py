def print_inverted_triangle(size: int) -> str:
    if size <= 0:
        return ""
    lines = []
    for i in range(size, 0, -1):
        lines.append("*" * i)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_size = 5
    print(print_inverted_triangle(sample_size))
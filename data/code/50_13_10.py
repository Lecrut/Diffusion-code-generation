def build_inverted_right_angled_triangle(n):
    if n <= 0:
        return ""
    lines = []
    for i in range(n, 0, -1):
        lines.append("*" * i)
    return "\n".join(lines)

if __name__ == '__main__':
    size = 5
    result = build_inverted_right_angled_triangle(size)
    print(result)
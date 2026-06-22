def build_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        num_str = str(i)
        line_content = " ".join(str(j) for j in range(1, i + 1))
        spaces = " " * (height - i)
        lines.append(f"{spaces}{line_content}{spaces}")
    return "\n".join(lines)

if __name__ == '__main__':
    result = build_pyramid(7)
    print(result)
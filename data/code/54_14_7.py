def render_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    lines = [top_bottom]
    for _ in range(size - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    result = render_hollow_square(5)
    print(result)
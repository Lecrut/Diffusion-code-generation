def render_hollow_square(size):
    if size < 1:
        return ""
    if size == 1:
        return "*"
    border = "*" * size
    inner = "*" + " " * (size - 2) + "*"
    lines = []
    lines.append(border)
    for _ in range(size - 2):
        lines.append(inner)
    lines.append(border)
    return "\n".join(lines)

if __name__ == '__main__':
    print(render_hollow_square(5))
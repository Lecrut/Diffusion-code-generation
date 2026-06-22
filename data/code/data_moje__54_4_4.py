def make_hollow_square(size=10):
    if size <= 0:
        return ""
    border = "#" * size
    inner = "#" + "." * (size - 2) + "#"
    lines = [border]
    for _ in range(size - 2):
        lines.append(inner)
    if size > 1:
        lines.append(border)
    return "\n".join(lines)

if __name__ == '__main__':
    print(make_hollow_square(10))
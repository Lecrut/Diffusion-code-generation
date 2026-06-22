def render_hollow_square(size):
    if size < 1:
        return ""
    if size == 1:
        return "*"
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    lines = [top_bottom] + [middle] * (size - 2) + [top_bottom]
    return "\n".join(lines)

if __name__ == '__main__':
    print(render_hollow_square(5))
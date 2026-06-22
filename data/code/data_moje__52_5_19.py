def render_diamond_fixed():
    center = 3
    offset = center - 1
    lines = []
    for delta in range(-offset, offset + 1):
        spaces = abs(delta)
        stars = center - spaces
        lines.append(" " * spaces + "*" * (2 * stars - 1))
    return "\n".join(lines)

if __name__ == '__main__':
    print(render_diamond_fixed())
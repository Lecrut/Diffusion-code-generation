def render_diamond(height):
    if height <= 0:
        return ""
    lines = []
    for i in range(-height + 1, height):
        spaces = abs(i)
        stars = 2 * (height - abs(i)) - 1
        lines.append(" " * spaces + "*" * stars)
    return "\n".join(lines)

if __name__ == "__main__":
    result = render_diamond(3)
    print(result)
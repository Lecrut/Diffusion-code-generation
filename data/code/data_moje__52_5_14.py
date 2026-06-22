def render_diamond():
    size = 3
    lines = []
    for i in range(-size, size + 1):
        spaces = " " * abs(i)
        stars = "*" * (size + 1 - abs(i) * 2) if abs(i) < size else "*"
        if stars:
            lines.append(spaces + stars)
        else:
            lines.append(spaces + "*")
    return "\n".join(lines)

if __name__ == "__main__":
    result = render_diamond()
    print(result)
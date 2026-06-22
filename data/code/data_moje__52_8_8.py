def render_diamond(height):
    result = []
    for i in range(height):
        spaces = " " * (height // 2 - i) if i <= height // 2 else " " * (i - height // 2)
        stars = "*" * (2 * i + 1) if i <= height // 2 else "*" * (2 * (height - i) - 1)
        line = spaces + stars + spaces
        result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    height = 7
    print(render_diamond(height))
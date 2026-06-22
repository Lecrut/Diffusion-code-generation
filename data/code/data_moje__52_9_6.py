def generate_diamond(half_height):
    lines = []
    for i in range(1, half_height + 1):
        spaces = " " * (half_height - i)
        stars = "* " * i
        lines.append(spaces + stars.strip())
    for i in range(half_height - 1, 0, -1):
        spaces = " " * (half_height - i)
        stars = "* " * i
        lines.append(spaces + stars.strip())
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_diamond(4)
    print(result)
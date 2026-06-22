def generate_diamond(radius: int) -> str:
    lines = []
    for i in range(-radius, radius + 1):
        stars = radius - abs(i)
        spaces = abs(i)
        line = " " * spaces + "* " * stars + "* " * spaces
        lines.append(line.rstrip())
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_diamond(4)
    print(result)
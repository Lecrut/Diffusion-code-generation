def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    lines = []
    for i in range(size):
        if i == 0 or i == size - 1:
            lines.append("*" * size)
        else:
            line = "*" + " " * (size - 2) + "*"
            lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_hollow_square(5))
    print(generate_hollow_square(1))
    print(generate_hollow_square(3))
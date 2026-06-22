def construct_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "#"
    row = "#" * size
    middle = "#" + "." * (size - 2) + "#"
    lines = [row]
    for _ in range(size - 2):
        lines.append(middle)
    lines.append(row)
    return "\n".join(lines)

if __name__ == '__main__':
    print(construct_hollow_square(10))
def create_symmetric_pyramid(levels=4):
    if levels < 1:
        return ""
    lines = []
    for i in range(1, levels + 1):
        line = " " * (levels - i)
        line += "1"
        if i > 1:
            for digit in "23456789":
                line += digit
            line = line[:2 * i - 1]
            for j in range(2 * i - 3, -1, -1):
                line += line[j]
            line += "1"
            line = line[:2 * i - 1]
        spaces = " " * (levels - i)
        lines.append(spaces + line)
    return "\n".join(lines)

if __name__ == '__main__':
    pyramid = create_symmetric_pyramid(4)
    print(pyramid)
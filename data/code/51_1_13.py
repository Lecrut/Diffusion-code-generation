def create_symmetric_number_pyramid(levels):
    lines = []
    for i in range(1, levels + 1):
        line = ""
        for _ in range(levels - i):
            line += " "
        current_level = i
        for _ in range(i):
            line += str(current_level)
        line += str(current_level - 1) if current_level > 1 else ""
        while current_level > 1:
            current_level -= 1
            line += str(current_level)
        lines.append(line)
    result = ""
    for i in range(len(lines) - 1, -1, -1):
        result += lines[i] + "\n"
    return result.rstrip()

if __name__ == '__main__':
    print(create_symmetric_number_pyramid(4))
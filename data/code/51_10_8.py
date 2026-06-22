def generate_number_pyramid(height):
    lines = []
    max_width = 2 * height - 1
    for i in range(1, height + 1):
        number = i
        row_str = str(number)
        padding = max_width - 2 * len(row_str)
        if padding < 0:
            padding = 0
        space = padding // 2
        line = " " * space + row_str + " " * space
        lines.append(line.rstrip())
    return "\n".join(lines)

if __name__ == "__main__":
    print(generate_number_pyramid(5))
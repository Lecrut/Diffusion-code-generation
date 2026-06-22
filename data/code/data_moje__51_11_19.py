def construct_pyramid(height: int) -> str:
    max_width = 2 * height - 1
    lines = []
    for i in range(1, height + 1):
        numbers = list(range(1, i + 1))
        row_str = " ".join(str(n) for n in numbers)
        spaces = (max_width - len(row_str)) // 2
        line = " " * spaces + row_str + " " * spaces
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = construct_pyramid(7)
    print(result)
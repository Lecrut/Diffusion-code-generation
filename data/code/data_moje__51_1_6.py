def create_symmetric_number_pyramid(levels):
    if levels <= 0:
        return ""
    lines = []
    for i in range(1, levels + 1):
        numbers = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        line = " ".join(str(n) for n in numbers)
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = create_symmetric_number_pyramid(4)
    print(result)
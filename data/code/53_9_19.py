def print_reverse_number_triangle(height: int = 5) -> list[str]:
    lines: list[str] = []
    for i in range(height, 0, -1):
        line = ' '.join(str(j) for j in range(i, 0, -1))
        lines.append(line)
    for line in lines:
        print(line)
    return lines

if __name__ == '__main__':
    print_reverse_number_triangle(5)
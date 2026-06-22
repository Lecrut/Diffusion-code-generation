def build_symmetric_pyramid(rows=6):
    lines = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = list(range(1, i + 1))
        right_part = numbers[-2::-1]
        row_nums = [str(n) for n in numbers + right_part]
        row_str = ' '.join(row_nums)
        line = spaces + row_str
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(build_symmetric_pyramid(6))
def generate_number_pyramid(rows: int = 3) -> str:
    lines = []
    max_width = rows * 2 - 1
    for i in range(1, rows + 1):
        nums = list(range(1, i + 1))
        line = ' '.join(str(n) for n in nums)
        lines.append(line.center(max_width))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_number_pyramid(3))
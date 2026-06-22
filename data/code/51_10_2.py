def generate_number_pyramid(rows: int = 5) -> str:
    lines = []
    for i in range(1, rows + 1):
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        line = numbers.center((rows * 2) - 1)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_number_pyramid())